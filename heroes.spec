%bcond_without	ggi	# without ggi support
%bcond_without	sdl	# without sdl support

Summary:	Game like Nibbles
Summary(pl.UTF-8):   Gra w stylu Nibbles
Name:		heroes
Version:	0.21
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/heroes/%{name}-%{version}.tar.bz2
Patch0:		%{name}-gkh.patch
# Source0-md5:	ec608676e2e75abdfddf8072bb3b28db
URL:		http://heroes.sourceforge.net/
%if %{with sdl}
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
%endif
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext
%if %{with ggi}
BuildRequires:	libggi-devel
BuildRequires:	libgii-devel
BuildRequires:	libmikmod-devel
%endif
Requires:	%{name}-data
Requires:	%{name}-engine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features. In it, you
must maneuver a small vehicle around a world and collect powerups
while avoiding obstacles, your opponents' trails, and even your own
trail. Several modes of play are available, including
"get-all-the-bonuses", deathmatch, and "squish-the-pedestrians".

%description -l pl.UTF-8
Heroes jest podobny do starych gier "Tron" i "Nibbles", ale zawiera
wiele graficznych ulepszeń i nowe własności. W tej grze musisz
manewrować małym pojazdem i zbierać dopalacze, unikając przeszkód i
śladów przeciwników, a nawet swojego własnego śladu. Są dostępne różne
tryby gry, w tym "zbierz-wszystkie-premie", deathmatch oraz
"rozjedź-pieszych".

%package sdl
Summary:	Game like Nibbles but different - SDL engine
Summary(pl.UTF-8):   Gra w stylu Nibbles, ale inna - wersja SDL
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-engine

%description sdl
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features. In it, you
must maneuver a small vehicle around a world and collect powerups
while avoiding obstacles, your opponents' trails, and even your own
trail. Several modes of play are available, including
"get-all-the-bonuses", deathmatch, and "squish-the-pedestrians". This
package containts SDL engine.

%description sdl -l pl.UTF-8
Heroes jest podobny do starych gier "Tron" i "Nibbles", ale zawiera
wiele graficznych ulepszeń i nowe własności. W tej grze musisz
manewrować małym pojazdem i zbierać dopalacze, unikając przeszkód i
śladów przeciwników, a nawet swojego własnego śladu. Są dostępne różne
tryby gry, w tym "zbierz-wszystkie-premie", deathmatch oraz
"rozjedź-pieszych". Pakiet zawiera wersję SDL gry.

%package ggi
Summary:	Game like Nibbles but different - GGI engine
Summary(pl.UTF-8):   Gra w stylu Nibbles, ale inna - wersja GGI
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-engine

%description ggi
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features. In it, you
must maneuver a small vehicle around a world and collect powerups
while avoiding obstacles, your opponents' trails, and even your own
trail. Several modes of play are available, including
"get-all-the-bonuses", deathmatch, and "squish-the-pedestrians". This
package containts GGI engine.

%description ggi -l pl.UTF-8
Heroes jest podobny do starych gier "Tron" i "Nibbles", ale zawiera
wiele graficznych ulepszeń i nowe własności. W tej grze musisz
manewrować małym pojazdem i zbierać dopalacze, unikając przeszkód i
śladów przeciwników, a nawet swojego własnego śladu. Są dostępne różne
tryby gry, w tym "zbierz-wszystkie-premie", deathmatch oraz
"rozjedź-pieszych". Pakiet zawiera wersję ggi gry

%prep
%setup -q
%patch0

%build
cp -f /usr/share/automake/config.sub tools
%if %{with ggi}
%configure \
	--with-ggi \
	--with-gii \
	--with-mikmod \
	--without-sdl \
	--without-sdl-mixer
%{__make}
mv src/heroes src/heroes-ggi
%endif

%if %{with sdl}
%configure \
	--without-ggi \
	--without-gii \
	--without-mikmod \
	--with-sdl \
	--with-sdl-mixer
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with ggi}
install src/%{name}-ggi $RPM_BUILD_ROOT%{_bindir}/%{name}-ggi
%endif

%if %{with sdl}
mv $RPM_BUILD_ROOT%{_bindir}/%{name}{,-sdl}
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/%{name}lvl
%{_mandir}/man?/%{name}*
%{_infodir}/%{name}*
%{_datadir}/%{name}

%if %{with sdl}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-sdl
%endif

%if %{with ggi}
%files ggi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-ggi
%endif
