Summary:	Game like Nibbles but different
Summary(pl):	Gra w stylu Nibbles, ale inna
Name:		heroes
Version:	0.21
Release:	1.1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/heroes/%{name}-%{version}.tar.bz2
# Source0-md5:	ec608676e2e75abdfddf8072bb3b28db
URL:		http://heroes.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext
BuildRequires:	libggi-devel
BuildRequires:	libgii-devel
Requires:	%{name}-data
Requires:	%{name}-sound-effects
Requires:	%{name}-sound-tracks
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features. In it, you
must maneuver a small vehicle around a world and collect powerups
while avoiding obstacles, your opponents' trails, and even your own
trail. Several modes of play are available, including
"get-all-the-bonuses", deathmatch, and "squish-the-pedestrians".

%description -l pl
Heroes jest podobny do starych gier "Tron" i "Nibbles", ale zawiera
wiele graficznych ulepszeñ i nowe w³asno¶ci. W tej grze musisz
manewrowaæ ma³ym pojazdem i zbieraæ dopalacze, unikaj±c przeszkód i
¶ladów przeciwników, a nawet swojego w³asnego ¶ladu. S± dostêpne ró¿ne
tryby gry, w tym "zbierz-wszystkie-premie", deathmatch oraz
"rozjed¼-pieszych".

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub tools
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/%{name}*
%{_infodir}/%{name}*
%{_datadir}/%{name}
