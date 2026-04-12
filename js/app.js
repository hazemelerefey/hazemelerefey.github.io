function appData() {
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

        serviceRequest: {
            selected: ''
        },

        // Interactive Rating State
        ratings: {
            portfolio: {
                score: 0,
                hoverScore: 0,
                totalVotes: 35,
                average: 5.0
            },
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
            jobpulse: {
                score: 0,
                hoverScore: 0,
                totalVotes: 76,
                average: 4.9
            },
            kanban: {
                score: 0,
                hoverScore: 0,
                totalVotes: 58,
                average: 4.8
            },
            realestate: {
                score: 0,
                hoverScore: 0,
                totalVotes: 63,
                average: 4.8
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

        // --- Premium Project Story Data (Liquid Glass Gallery) ---
        projectsList: [
            {
                id: 'jobpulse',
                title: 'JobPulse',
                image: 'images/jobpulse-hero.svg',
                category: 'frontend',
                tags: ['Market Intelligence', 'Next.js'],
                github: 'https://github.com/hazemelerefey/jobpulse',
                color: 'cyan',
                ratingKey: 'jobpulse',
                story: 'In an increasingly saturated tech market, job seekers often feel like they are shouting into the void. JobPulse was conceived as a premium intelligence dashboard, rather than a generic job board. By aggregating and analyzing live role demand, compensation shifts, and remote-work trends, it transforms overwhelming market noise into a sleek, actionable, product-style interface that empowers users to make precise career decisions.',
                features: ['Live Role Demand Metrics', 'Compensation Gravity tracking', 'Skill Momentum indicators', 'Polished, glassmorphic UI architecture', 'Fully repo-backed static build']
            },
            {
                id: 'healthcare',
                title: 'Healthcare Waitlist',
                image: 'images/healthcare-operations-overview.png',
                category: 'analytics',
                tags: ['Healthcare', 'Power BI'],
                github: 'https://github.com/hazemelerefey/healthcare-operations-waitlist-dashboard',
                color: 'emerald',
                ratingKey: 'healthcare',
                story: 'Patient care delays aren\'t just numbers; they represent human lives waiting for help. When a hospital faces massive waitlist pressure, standard messy spreadsheets fail to provide operational clarity. This analytics dashboard was designed to act as an executive decision-support system. It cuts through the fog of data to instantly reveal service bottlenecks, specialty backlog patterns, and critical operational priorities.',
                features: ['Waitlist Pressure heatmapping', 'Service Bottleneck identification', 'Specialty Backlog pattern analysis', 'Clinical decision-support layout', 'Operational metrics tracking']
            },
            {
                id: 'kanban',
                title: 'Kanban Board',
                image: 'images/kanban-project.svg',
                category: 'frontend',
                tags: ['Kanban UI', 'Frontend'],
                github: 'https://github.com/hazemelerefey/frontend-kanban-board',
                color: 'cyan',
                ratingKey: 'kanban',
                story: 'Productivity apps often suffer from visual clutter, hindering focus when you need it most. This frontend Kanban board was built as an exploration into product-style interfaces where fluidity and clarity are paramount. Utilizing seamless drag-and-drop mechanics and a highly polished administrative layout, it creates a distraction-free environment for task management.',
                features: ['Fluid drag-and-drop workflow mechanics', 'Product-style layout typography', 'High-contrast board clarity', 'Interactive task progression tracking', 'Clean administrative composition']
            },
            {
                id: 'realestate',
                title: 'Real Estate Finder',
                image: 'images/realestate-project.svg',
                category: 'frontend',
                tags: ['Real Estate UI', 'Frontend'],
                github: 'https://github.com/hazemelerefey/frontend-realestate-finder',
                color: 'purple',
                ratingKey: 'realestate',
                story: 'Searching for a home is an emotional, high-stakes journey that demands a flawless digital experience. This real estate interface bridges the gap between raw property data and human exploration. It heavily features advanced filtering mechanisms and listing discovery paradigms within an elegant, minimal product-style aesthetic for swift property comparison.',
                features: ['Advanced filtering architecture', 'Listing discovery map patterns', 'Product-style property browsing', 'High-fidelity image presentation', 'Minimalist visual layout']
            },
            {
                id: 'global_sales',
                title: 'Global Sales Tracker',
                image: 'images/global-sales-dashboard.png',
                category: 'analytics',
                tags: ['Commercial BI', 'Power BI'],
                github: 'https://github.com/hazemelerefey/global-ecommerce-sales-tracker',
                color: 'amber',
                ratingKey: 'global_sales',
                story: 'When an e-commerce platform scales globally, tracking revenue becomes a fragmented nightmare across multiple regions. This interactive Business Intelligence dashboard acts as the central command center. By deeply analyzing regional commercial performance, profit margins, and order fulfillment vectors, it allows stakeholders to steer massive enterprise-level sales operations with granular precision.',
                features: ['Multi-region revenue tracking', 'Profit margin optimization metrics', 'Order fulfillment vector analysis', 'Interactive commercial performance charts', 'Executive summary BI architecture']
            },
            {
                id: 'churn',
                title: 'Churn Prediction',
                image: 'images/churn-project.svg',
                category: 'analytics',
                tags: ['Machine Learning', 'Python'],
                github: 'https://github.com/hazemelerefey/analytics-churn-prediction',
                color: 'red',
                ratingKey: 'churn',
                story: 'Why do customers leave? That single question drives the billion-dollar retention industry. This project dives deep into predictive analytics to identify subtle behaviors that signal a user is about to churn. By highlighting critical risk patterns through machine learning feature importance mechanisms, businesses can shift from reacting to lost customers to proactively saving them.',
                features: ['Predictive risk modeling algorithms', 'Customer retention behavior analysis', 'Feature importance identification tools', 'Proactive churn mitigation signals', 'Data-driven decision support']
            },
            {
                id: 'ecommerce',
                title: 'E-Commerce Admin UI',
                image: 'images/ecommerce-admin-project.svg',
                category: 'frontend',
                tags: ['React Admin UI', 'Frontend'],
                github: 'https://github.com/hazemelerefey/frontend-ecommerce-dashboard',
                color: 'cyan',
                ratingKey: 'ecommerce',
                story: 'Backend administrative tools have historically been clunky and visually uninspiring. This UI challenges that norm by bringing consumer-grade premium design to the backend. It offers a pristine, responsive dashboard interface tailored for store managers—making the monitoring of sales velocity, active orders, and user activity an engaging, rather than exhausting, daily task.',
                features: ['Responsive frontend administration', 'Live sales velocity monitoring', 'Dynamic chart integration', 'User activity tracking modules', 'Product-ready layout composition']
            }
        ],

        // --- Liquid Glass Story Modal States ---
        storyModalOpen: false,
        activeStory: null,

        openStory(project) {
            this.activeStory = project;
            this.storyModalOpen = true;
            document.body.style.overflow = 'hidden';
        },

        closeStory() {
            this.storyModalOpen = false;
            // Restore background scrolling
            document.body.style.overflow = '';
            setTimeout(() => {
                this.activeStory = null;
            }, 500); // 500ms aligns with Liquid Glass animation speed
        },

        getEmotion(project) {
            return this.ratings[project].hoverScore || this.ratings[project].score || 0;
        },

        setRating(project, stars) {
            const rating = this.ratings[project];
            const currentAverage = parseFloat(rating.average);

            if (rating.score === 0) {
                rating.score = stars;
                rating.totalVotes++;
                const newTotal = (currentAverage * (rating.totalVotes - 1)) + stars;
                rating.average = (newTotal / rating.totalVotes).toFixed(1);
            } else {
                const oldScore = rating.score;
                rating.score = stars;
                const oldTotal = currentAverage * rating.totalVotes;
                const newTotal = oldTotal - oldScore + stars;
                rating.average = (newTotal / rating.totalVotes).toFixed(1);
            }

            rating.hoverScore = stars;
        },
        hoverStar(project, stars) {
            this.ratings[project].hoverScore = stars;
        },
        resetHover(project) {
            this.ratings[project].hoverScore = this.ratings[project].score || 0;
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



        navTo(view) {
            this.activeView = view;
            this.mobileMenuOpen = false;

            // Smooth scroll to top on navigation
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });

            // Refresh AOS animations for the new content
            setTimeout(() => {
                if (typeof AOS !== 'undefined') {
                    AOS.refresh();
                }
            }, 400); 
        },

        openServiceRequest(service = '') {
            this.activeView = 'services';
            this.mobileMenuOpen = false;
            this.serviceRequest.selected = service;

            setTimeout(() => {
                const section = document.getElementById('request-service');
                if (section) {
                    section.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
                if (typeof AOS !== 'undefined') {
                    AOS.refresh();
                }
            }, 120);
        },

        submitProjectRequest(event) {
            const form = event.target;
            const data = new FormData(form);
            const name = (data.get('name') || '').toString().trim();
            const email = (data.get('email') || '').toString().trim();
            const budget = (data.get('budget') || '').toString().trim() || 'Not specified';
            const timeline = (data.get('timeline') || '').toString().trim() || 'Not specified';
            const service = (data.get('service') || this.serviceRequest.selected || 'General project inquiry').toString().trim();
            const details = (data.get('details') || '').toString().trim();

            const subject = encodeURIComponent(`Project Inquiry - ${service}`);
            const body = encodeURIComponent(
`Name: ${name}
Email: ${email}
Service Needed: ${service}
Budget Range: ${budget}
Timeline: ${timeline}

Project Details:
${details}`
            );

            window.location.href = `mailto:hazemkhaled53@gmail.com?subject=${subject}&body=${body}`;
        },


        init() {


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
}
