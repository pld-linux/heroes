%define name heroes
%define version 0.12
%define release 2mdk

Summary: Game like Nibbles but different.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.sourceforge.net/heroes/%{name}-%{version}.tar.bz2
Source1: http://download.sourceforge.net/heroes/%{name}-data-1.1.tar.bz2
Source2: http://download.sourceforge.net/heroes/%{name}-sound-tracks-1.0.tar.bz2
Source3: http://download.sourceforge.net/heroes/%{name}-sound-effects-1.0.tar.bz2
Copyright: GPL
Packager: Pixel <pixel@mandrakesoft.com>
Url: http://heroes.sourceforge.net/
Group: Games/Arcade
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildRequires: gettext bison libSDL-devel libSDL_mixer-devel

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but includes
many graphical improvements and new game features.  In it, you must
maneuver a small vehicle around a world and collect powerups while avoiding
obstacles, your opponents' trails, and even your own trail. Several modes
of play are available, including "get-all-the-bonuses", deathmatch, and
"squish-the-pedestrians".

%prep
%setup -q
%setup -q -D -T -a 1
%setup -q -D -T -a 2
%setup -q -D -T -a 3

%build
%configure
%make
    (cd %{name}-data-1.1
     %configure
     %make
    )       
for i in sound-effects sound-tracks; do
    (
    cd %{name}-$i-1.0
    %configure
    %make
    )
done

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
    (cd %{name}-data-1.1
     %makeinstall
    )
for i in sound-effects sound-tracks; do
    (
    cd %{name}-$i-1.0
    %makeinstall
    )
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL NEWS README THANKS TODO
%{_datadir}/%{name}
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Thu Jul 12 2001 Daouda LO <daouda@mandrakesoft.com> 0.12-2mdk
- update heroes source data to 1.1.
- provides mising icons.

* Wed Jul 11 2001  Daouda Lo <daouda@mandrakesoft.com> 0.12-1mdk
- new version.

* Tue Jul  3 2001 Pixel <pixel@mandrakesoft.com> 0.11-1mdk
- new version

* Mon May 14 2001 Pixel <pixel@mandrakesoft.com> 0.10-2mdk
- rebuild with new SDL

* Tue May  8 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.10-1mdk
- version 0.10

* Mon Mar  5 2001 Pixel <pixel@mandrakesoft.com> 0.9-2mdk
- add mo files (thanks to Alexandre Duret-Lutz)

* Sat Mar  3 2001 Pixel <pixel@mandrakesoft.com> 0.9-1mdk
- new version

* Wed Dec 20 2000 Pixel <pixel@mandrakesoft.com> 0.8-1mdk
- new version

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 0.7-2mdk
- rebuild with new libSDL_mixer

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 0.7-1mdk
- initial spec


# end of file
