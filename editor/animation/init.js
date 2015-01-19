//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210', 'snap.svg_030'],
    function (ext, $, Raphael, Snap) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide = {};
            cur_slide["in"] = data[0];
            this_e.addAnimationSlide(cur_slide);
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var ends = ["th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th"]

            options = options || {};
            var is_new_record = options.is_new_record || false;
            var place_rating = String(options.place_rating || 0);
            var best_points = options.best_points || 0;
            var current_points = options.current_points || 0;
            var $div = $("<div></div>");
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div class="result"></div></div>'));
            var $resultDiv = $h.find(".result");
            var $table = $("<table></table>").addClass("numbers");
            if (is_new_record) {
                $resultDiv.addClass("win-sign");
                $resultDiv.append($("<div></div>").text("You beat your best results!"));
                var $tr = $("<tr></tr>");
                $tr.append($("<th></th>").text(best_points));
                $tr.append($("<th></th>").text(place_rating).append($("<span></span>").addClass(".ends").text(ends[Number(place_rating[place_rating.length - 1])])));

                $table.append($tr);
                $tr = $("<tr></tr>");
                $tr.append($("<td></td>").text("Personal best"));
                $tr.append($("<td></td>").text("Place"));
                $table.append($tr);
            }
            else {
                $resultDiv.addClass("norm-sign");
                $resultDiv.append($("<div></div>").text("Your results"));
                $tr = $("<tr></tr>");
                $tr.append($("<th></th>").text(current_points));
                $tr.append($("<th></th>").text(best_points));
                $tr.append($("<th></th>").text(place_rating).append($("<span></span>").addClass(".ends").text(ends[Number(place_rating[place_rating.length - 1])])));

                $table.append($tr);
                $tr = $("<tr></tr>");
                $tr.append($("<td></td>").text("Points"));
                $tr.append($("<td></td>").text("Personal best"));
                $tr.append($("<td></td>").text("Place"));
                $table.append($tr);
            }
            $resultDiv.append($table);
            this_e.setAnimationHeight(255);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            //YOUR FUNCTION NAME
            var fname = 'gather_people';

            var checkioInput = data.in;
            var checkioInputStr = fname + '(' + JSON.stringify(checkioInput[0]) + ", " + checkioInput[1] + ")";

            var failError = function (dError) {
                $content.find('.call').html(checkioInputStr);
                $content.find('.output').html(dError.replace(/\n/g, ","));

                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.answer').remove();
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
            };

            if (data.error) {
                failError(data.error);
                return false;
            }

            if (data.ext && data.ext.inspector_fail) {
                failError(data.ext.inspector_result_addon);
                return false;
            }

            $content.find('.call').html(checkioInputStr);
            $content.find('.output').html('Working...');


            if (data.ext) {
                var rightResult = data.ext["answer"];
                var userResult = data.out;
                var result = data.ext["result"];
                var rooms = data.ext["rooms"];
                var paths = data.ext["paths"];
                var escaped = data.ext["escaped"];


                var svg = new SVG($content.find(".explanation")[0]);

                svg.draw(rooms, paths, escaped);

                $content.find('.output').html('&nbsp;Your result:&nbsp;' + JSON.stringify(userResult));
                if (!result) {
                    $content.find('.answer').html('Right result:&nbsp;' + JSON.stringify(rightResult));
                    $content.find('.answer').addClass('error');
                    $content.find('.output').addClass('error');
                    $content.find('.call').addClass('error');
                }
                else {
                    $content.find('.answer').remove();
                }
            }
            else {
                $content.find('.answer').remove();
            }


            //Your code here about test explanation animation
            //$content.find(".explanation").html("Something text for example");
            //
            //
            //
            //
            //


            this_e.setAnimationHeight($content.height() + 60);

        });

        //This is for Tryit (but not necessary)
//        var $tryit;
//        ext.set_console_process_ret(function (this_e, ret) {
//            $tryit.find(".checkio-result").html("Result<br>" + ret);
//        });
//
//        ext.set_generate_animation_panel(function (this_e) {
//            $tryit = $(this_e.setHtmlTryIt(ext.get_template('tryit'))).find('.tryit-content');
//            $tryit.find('.bn-check').click(function (e) {
//                e.preventDefault();
//                this_e.sendToConsoleCheckiO("something");
//            });
//        });

        function SVG(dom) {
            var colorOrange4 = "#F0801A";
            var colorOrange3 = "#FA8F00";
            var colorOrange2 = "#FAA600";
            var colorOrange1 = "#FABA00";

            var colorBlue4 = "#294270";
            var colorBlue3 = "#006CA9";
            var colorBlue2 = "#65A1CF";
            var colorBlue1 = "#8FC7ED";

            var colorGrey4 = "#737370";
            var colorGrey3 = "#9D9E9E";
            var colorGrey2 = "#C5C6C6";
            var colorGrey1 = "#EBEDED";

            var colorWhite = "#FFFFFF";

            var pad = 5;

            var roomRadius = 15;

            var cellSize = 37;
            var sizeX = 370 + 2 * pad;
            var sizeY;

            var paper;

            var aWall = {"stroke": colorBlue4, "stroke-width": 4};
            var aGoodPath = {"stroke": colorBlue4, "stroke-width": 5};
            var aBadPath = {"stroke": colorOrange4, "stroke-width": 5};
            var aText = {
                "stroke": colorBlue4, "font-family": "Roboto, Arial, open-serif",
                "font-weight": "bold", "font-size": roomRadius * 1.5
            };
            var aBadRoom = {"stroke": colorGrey4, "fill": colorGrey2, "stroke-width": 2};
            var aGoodRoom = {"stroke": colorGrey4, "fill": colorBlue2, "stroke-width": 2};

            this.draw = function (rooms, paths, escaped) {
                var minX = Infinity;
                var minY = Infinity;
                var maxX = -Infinity;
                var maxY = -Infinity;
                for (var i = 0; i < rooms.length; i++) {
                    var r = rooms[i];
                    minX = r[0] < minX ? r[0] : minX;
                    maxX = r[0] > maxX ? r[0] : maxX;
                    minY = r[1] < minY ? r[1] : minY;
                    maxY = r[1] > maxY ? r[1] : maxY;
                }


                cellSize = Math.max(370 / (maxX - minX + 2), cellSize);
                sizeY = (maxY - minY + 2) * cellSize + 2 * pad;

                paper = Raphael(dom, sizeX, sizeY);


                //console.log(minX, maxX, minY, maxY);
                //console.log(cellSize);

                paper.rect(pad, pad, sizeX - 2 * pad, sizeY - 2 * pad).attr(aWall);

                for (i = 0; i < paths.length; i++) {
                    var f = paths[i][0];
                    var s = paths[i][1];
                    var p = paper.path([["M", pad + (rooms[f][0] - minX + 1) * cellSize,
                        pad + (rooms[f][1] - minY + 1) * cellSize],
                        ["L", pad + (rooms[s][0] - minX + 1) * cellSize, pad + (rooms[s][1] - minY + 1) * cellSize]]);
                    if (escaped.indexOf(f) === -1 || escaped.indexOf(s) === -1) {
                        p.attr(aBadPath);
                    }
                    else {
                        p.attr(aGoodPath);
                    }
                }
                for (i = 0; i < rooms.length; i++) {
                    paper.circle(pad + cellSize * (rooms[i][0] - minX + 1), pad + cellSize * (rooms[i][1] - minY + 1), roomRadius).attr(
                        escaped.indexOf(i) === -1 ? aBadRoom : aGoodRoom);
                    paper.text(pad + cellSize * (rooms[i][0] - minX + 1), pad + cellSize * (rooms[i][1] - minY + 1), rooms[i][2]).attr(aText);

                }
            }

        }


        //Your Additional functions or objects inside scope
        //
        //
        //


    }
);
