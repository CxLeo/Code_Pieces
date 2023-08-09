    return (
        <ThemeProvider theme={uofaTheme}>
            <CssBaseline />
            <AppBar position='relative' color='primary'>
                <Toolbar style={{background: 'linear-gradient(to right top, #fcfcfc, #3c6d99)'}}>
                    <Box
                        component='img'
                        sx={{ height: 45, marginRight:5 }}
                        alt='UofA'
                        src={logo}
                    />
                    <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
                        {tabs.map((tab : string) => (
                            tab === 'Admin' ?
                                <Button
                                    key={tab}
                                    sx={{ my: 2, color: 'black', display: 'block' }}
                                    onClick={() => {
                                        let path;
                                        //console.log(cookies.user);
                                        if (cookies.user) {
                                            path = '/admin';
                                        } else {
                                            path = '/adminsignin';
                                        }
                                        navigate(path);
                                    }}
                                >
                                    {tab}
                                </Button>
                                : 
                                <h1></h1>
                        ))}
                    </Box>
                </Toolbar>
            </AppBar>
            <main>
                <Hero />
                <Perspective/>
                <Planning/>
                <Programming/>
                <Footer/>
            </main>
        </ThemeProvider>
    );
}

export default LandingPage;
