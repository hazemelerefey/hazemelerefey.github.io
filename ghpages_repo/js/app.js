(() => {


    document.addEventListener('alpine:init', () => {
        window.appData = function () {
            return {
                mobileMenuOpen: false,
                scrolled: false,

                activeView: 'home', // Start on the Home tab
                workspaceTab: 'frontend',
                portfolioFilter: 'all', // 'all', 'frontend', 'analytics'
                zoomModalOpen: false,
                zoomedImageSrc: '',

                // Dashboard Modal State
                dashboardModalOpen: false,
                activeDashboard: '', // 'healthcare' or 'global_sales'

                // Interactive Rating State
                ratings: {
                    healthcare: {
                        score: 0,
                        hoverScore: 0,
                        totalVotes: 124,
                        average: 4.8
                    },
                    global_sales: {
                        score: 0,
                        hoverScore: 0,
                        totalVotes: 89,
                        average: 4.9
                    },
                    ecommerce: {
                        score: 0,
                        hoverScore: 0,
                        totalVotes: 245,
                        average: 4.9
                    },
                    saas: {
                        score: 0,
                        hoverScore: 0,
                        totalVotes: 112,
                        average: 4.8
                    },
                    real_estate: {
                        score: 0,
                        hoverScore: 0,
                        totalVotes: 88,
                        average: 5.0
                    },
                    churn: {
                        score: 0,
                        hoverScore: 0,
                        totalVotes: 64,
                        average: 4.7
                    }
                },
                getEmotion(project) {
                    return this.ratings[project].hoverScore || this.ratings[project].score || 0;
                },

                setRating(project, stars) {
                    if (this.ratings[project].score === 0) {
                        this.ratings[project].score = stars;
                        this.ratings[project].totalVotes++;
                        let newTotal = (this.ratings[project].average * (this.ratings[project].totalVotes - 1)) + stars;
                        this.ratings[project].average = (newTotal / this.ratings[project].totalVotes).toFixed(1);
                    } else {
                        // User is changing their existing rating
                        let oldScore = this.ratings[project].score;
                        this.ratings[project].score = stars;
                        let oldTotal = this.ratings[project].average * this.ratings[project].totalVotes;
                        let newTotal = oldTotal - oldScore + stars;
                        this.ratings[project].average = (newTotal / this.ratings[project].totalVotes).toFixed(1);
                    }
                },
                hoverStar(project, stars) {
                    this.ratings[project].hoverScore = stars;
                },
                resetHover(project) {
                    this.ratings[project].hoverScore = 0;
                },

                openDashboard(type) {
                    this.activeDashboard = type;
                    this.dashboardModalOpen = true;
                    // Prevent background scrolling
                    document.body.style.overflow = 'hidden';
                },
                closeDashboard() {
                    this.dashboardModalOpen = false;
                    // Restore background scrolling
                    document.body.style.overflow = '';
                    setTimeout(() => {
                        this.activeDashboard = '';
                    }, 500); // Wait for transition to finish before clearing
                },



                init() {


                    // Refresh AOS animations when switching views
                    this.$watch('activeView', () => {
                        setTimeout(() => {
                            if (typeof AOS !== 'undefined') {
                                AOS.refresh();
                            }
                        }, 550); // Wait for the 500ms x-transition to finish
                    });
                },


                // Interactive Sitting Mascot Logic
                robotInteraction(dashboardId) {
                    return {
                        mouseYaw: 0,
                        mousePitch: 85,
                        trackMouse(e) {
                            if (!this.isHoveringCard || !this.$refs.card || !this.$refs.robotContainer) return;

                            const cardRect = this.$refs.card.getBoundingClientRect();
                            const robotRect = this.$refs.robotContainer.getBoundingClientRect();
                            const robotCenterX = robotRect.left + (robotRect.width / 2);
                            const robotCenterY = robotRect.top + (robotRect.height / 2);

                            const deltaX = e.clientX - robotCenterX;
                            const deltaY = e.clientY - robotCenterY;

                            // Max turn angles
                            const maxYaw = 45; // Max left/right
                            const maxPitch = 30; // Max up/down

                            // Linearly track mouse distance relative to the screen to aim head specifically at mouse
                            const normX = Math.max(-1, Math.min(1, deltaX / (window.innerWidth / 2)));
                            const normY = Math.max(-1, Math.min(1, deltaY / (window.innerHeight / 2)));

                            // Camera orbits opposite to the target gaze to fake the model turning
                            this.mouseYaw = -normX * maxYaw;
                            this.mousePitch = 85 + (-normY * maxPitch);
                        },
                        resetGaze() {
                            this.mouseYaw = 0;
                            this.mousePitch = 85;
                        },

                        // --- TWO-STATE HOVER ANIMATIONS ---
                        isHoveringCard: false,
                        animSrc: 'assets/models/sitting/Meshy_AI_Animation_Sit_and_Doze_Off_withSkin.glb',

                        hoverCard() {
                            this.isHoveringCard = true;
                            this.animSrc = 'assets/models/Meshy_AI_biped/Meshy_AI_Animation_Idle_withSkin.glb';

                            // Prevent the idle animation from swaying right/left, lock him standing perfectly still
                            this.$nextTick(() => {
                                if (this.$refs.robotViewer) {
                                    this.$refs.robotViewer.pause();
                                    this.$refs.robotViewer.currentTime = 0;
                                }
                            });
                        },

                        unhoverCard() {
                            this.isHoveringCard = false;
                            this.animSrc = 'assets/models/sitting/Meshy_AI_Animation_Sit_and_Doze_Off_withSkin.glb';

                            // Resume the sitting/dozing animation loop
                            this.$nextTick(() => {
                                if (this.$refs.robotViewer) {
                                    this.$refs.robotViewer.play();
                                }
                            });
                            this.resetGaze();
                        }
                    };
                }
            };
        };
    });
})();
