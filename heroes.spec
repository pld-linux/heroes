Summary:	Game like Nibbles but different
Summary(pl):	Gra w stylu Nibbles, ale inna
Name:		heroes
Version:	0.12
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/heroes/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.sourceforge.net/pub/sourceforge/heroes/%{name}-data-1.1.tar.bz2
Source2:	ftp://ftp.sourceforge.net/pub/sourceforge/heroes/%{name}-sound-tracks-1.0.tar.bz2
Source3:	ftp://ftp.sourceforge.net/pub/sourceforge/heroes/%{name}-sound-effects-1.0.tar.bz2
URL:		http://heroes.sourceforge.net/
BuildRequires:	gettext
BuildRequires:	bison
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
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
%setup -q -a1 -a2 -a3

%build
%configure
%{__make}

(cd %{name}-data-1.1
%configure
%{__make}
)

for i in sound-effects sound-tracks; do
(cd %{name}-$i-1.0
%configure
%{__make}
)
done

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
(cd %{name}-data-1.1
%makeinstall
)
for i in sound-effects sound-tracks; do
(cd %{name}-$i-1.0
%makeinstall
)
done

gzip -9nf CHANGES ChangeLog INSTALL NEWS README THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS* ChangeLog* INSTALL* NEWS* README* THANKS* TODO*
%{_datadir}/%{name}
%{_mandir}/*/*
%attr(755,root,root) %{_bindir}/*
