$fn = 50;


union() {
	translate(v = [0, 0, 0]) {
		projection() {
			intersection() {
				translate(v = [-500, -500, 1.5000000000]) {
					cube(size = [1000, 1000, 0.1000000000]);
				}
				difference() {
					union() {
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								cylinder(h = 4, r = 5);
							}
						}
					}
					union() {
						#translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								cylinder(h = 3, r1 = 3.0000000000, r2 = 2.5000000000);
							}
						}
						translate(v = [0, 0, 0]) {
							rotate(a = [0, 0, 0]) {
								translate(v = [0, 0, -50]) {
									rotate(a = [0, 0, 0]) {
										cylinder(h = 100, r = 1);
									}
								}
							}
						}
					}
				}
			}
		}
	}
}