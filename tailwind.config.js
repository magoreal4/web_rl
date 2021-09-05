module.exports = {
    purge: [
        './app/templates/**/*.html',
    ],
    darkMode: false,
    theme: {
        extend: {
            height: theme => ({
                'screen75': '75vh',
                'screen/2': '50vh',
                'screen/3': 'calc(100vh / 3)',
                'screen/4': 'calc(100vh / 4)',
                'screen/5': 'calc(100vh / 5)',
                'screen400': '400px',
                'screen600': '600px',
                'screen800': '800px',
                'screen1000': '1000px'
              }),
            fontFamily: {
                'nunito': ['"Nunito"','sans-serif']
            },
        },
        container: {
            center: true,
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
