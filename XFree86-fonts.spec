Summary:   XFree86 Fonts
%define    BASENAME XFree86
Name:      %BASENAME-fonts
Version:   3.3.3.1
Release:   2
Copyright: MIT
Group:     X11/XFree86/fonts
Group(pl): X11/XFree86/Fonty
Source:    ftp.xfree86.org:/pub/XFree86/3.3.3/source/X333src-2.tgz
Buildroot: /tmp/%name-%version-root
Patch:     XFree86-3.3.3-3.3.3.1.diff.fonts.gz
Prereq:    /usr/X11R6/bin/mkfontdir

Summary(pl): Fonty dla systemu XFree86 

%description 
This package contains the basic fonts, programs and documentation for an X
workstation. It does not provide the X server which drives your video
hardware -- those are available in other package.

%description -l pl

%package -n %BASENAME-75dpi-fonts
Summary:     X11R6 75dpi fonts - only need on server side
Group:       X11/XFree86/fonts
Group(pl):   X11/XFree86/Fonty
Summary(pl): Fonty o rozdzielczo¶ci 75dpi-niebêdne dla serwera.
Summary(de): X11RT 76 dpi-Fonts - nur auf Serverseite erforderlich
Summary(fr): Fontes 75 dpi X11R6 - nécessaire uniquement côté serveur
Summary(tr): X11R6 75dpi yazýtipleri - yalnýzca sunucu tarafýnda gerekir
Prereq:      /usr/X11R6/bin/mkfontdir
%ifarch sparc
Obsoletes:   X11R6.1-75dpi-fonts
%endif

%description -n %BASENAME-75dpi-fonts
The 75dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l de -n %BASENAME-75dpi-fonts
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. Für Benutzer
mit einer hochauflösender Darstellung sind die 100dpi-Fonts eines getrennt
erhältlichen Pakets besser geeignet.

%description -l fr -n %BASENAME-75dpi-fonts
Fontes 75 dpi utilisées sur la plupart des systèmes Linux. Ceux qui ont
des écrans à haute résolution préfèreront les fontes 100 dpi disponibles
dans un autre paquetage.

%description -l tr -n %BASENAME-75dpi-fonts
Çoðu Linux sisteminde 75dpi yazýtipi kullanýlýr. Yüksek çözünürlük kullanan
kullanýcýlar 100dpi yazýtiplerini yeðleyebilirler.

%description -l pl -n %BASENAME-75dpi-fonts
75dpi - Bazowe fonty dla wielu maszyn Linuxowych.
W wypadku wiêkszej rozdzielczo¶ci zaleczne fonty 100dpi dostêpne 
w oddzielnym pakiecie.

%package -n %BASENAME-100dpi-fonts
Summary:     X11R6 100dpi fonts - only need on server side
Group:       X11/XFree86/fonts
Group(pl):   X11/XFree86/Fonty
Summary(pl): Fonty o rozdzielczosci 100dpi-niezbêdne dla serwera.
Summary(de): X11R6 100dpi-Fonts - nur auf Server-Seite erforderlich
Summary(fr): Fontes 100ppp pour X11R6 - nécessaires seulement coté serveur.
Summary(tr): X11R6 100dpi yazýtipleri - yalnýzca sunucu tarafýnda gereklidir
Prereq:      /usr/X11R6/bin/mkfontdir
%ifarch sparc
Obsoletes:   X11R6.1-100dpi-fonts
%endif

%description -n %BASENAME-100dpi-fonts
The 100dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l pl -n %BASENAME-100dpi-fonts
100dpi - Bazowe fonty dla maszyn Linuxowych pracuj±cych w wysokiej 
rozdzielczo¶ci.

%description -l de -n %BASENAME-100dpi-fonts
Die 100dpi-Schriftarten, die auf den meisten Linux-Systemen zum Einsatz
kommen. Anwender mit hochauflösenden Monitoren ziehen unter Umständen
die 100dpi-Schriften vor, die in einem separaten Paket erhältlich sind.

%description -l fr -n %BASENAME-100dpi-fonts
Les fontes 100dpi sont utilisées par la plupart des systèmes Linux.
Les utilisateurs ayant des hautes résolutions peuvent préférer les 
fontes 100dpi disponibles dans un package séparé.

%description -l tr -n %BASENAME-100dpi-fonts
Yüksek çözünürlük kullanan kullanýcýlar 100dpi yazýtiplerini 75dpi olanlara
yeðleyebilirler.

%package -n %BASENAME-cyrillic-fonts
Summary:     X11R6 cyrillic fonts - only need on server side
Summary(de): X11R6 cyrillic-Fonts - nur auf Server-Seite erforderlich
Summary(fr): Fontes cyrillic pour X11R6 - nécessaires seulement coté serveur.
Summary(pl): X11R6 fonty 75dpi - wymagane tylko po stronie serwera
Summary(tr): X11R6 cyrillic yazýtipleri - yalnýzca sunucu tarafýnda gereklidir
Group:       X11/XFree86/fonts
Group(pl):   X11/XFree86/Fonty
Prereq:      /usr/X11R6/bin/mkfontdir

%description -n %BASENAME-cyrillic-fonts
The cyrillic fonts used on most Linux systems. Users with high resolution
displays may prefer the cyrillic fonts available in a separate package.

%description -l de -n %BASENAME-cyrillic-fonts
Die cyrillic-Schriftarten, die auf den meisten Linux-Systemen zum Einsatz
kommen. Anwender mit hochauflösenden Monitoren ziehen unter Umständen
die cyrillic-Schriften vor, die in einem separaten Paket erhältlich sind.

%description -l fr -n %BASENAME-cyrillic-fonts
Les fontes cyrillic sont utilisées par la plupart des systèmes Linux.
Les utilisateurs ayant des hautes résolutions peuvent préférer les 
fontes cyrillic disponibles dans un package séparé.

%description -l tr -n %BASENAME-cyrillic-fonts
Yüksek çözünürlük kullanan kullanýcýlar cyrillic yazýtiplerini 75dpi olanlara
yeðleyebilirler.

%description -l pl -n %BASENAME-cyrillic-fonts
Fonty cyrylicy s± u¿ywane na wiêkszo¶ci systemów linuxowych.

%prep
%setup -q -c 
%patch 

# Clean up to save a *lot* of disk space
find . -name "*.orig" -print | xargs rm -f
find . -size 0 -print | xargs rm -f

%build
cd xc/fonts
xmkmf
make Makefiles
make depend
make

%install
(cd xc/fonts;\
 make DESTDIR=$RPM_BUILD_ROOT install;\
 make DESTDIR=$RPM_BUILD_ROOT install.man;\
)


%files -n %BASENAME-fonts
%defattr(644, root, root, 755)
/usr/X11R6/lib/X11/fonts/Speedo
/usr/X11R6/lib/X11/fonts/Type1
/usr/X11R6/lib/X11/fonts/PEX
/usr/X11R6/lib/X11/fonts/misc

%files -n %BASENAME-75dpi-fonts
%defattr(644, root, root, 755)
/usr/X11R6/lib/X11/fonts/75dpi

%files -n %BASENAME-100dpi-fonts
%defattr(644, root, root, 755)
/usr/X11R6/lib/X11/fonts/100dpi

%files -n %BASENAME-cyrillic-fonts
%defattr(644, root, root, 755)
/usr/X11R6/lib/X11/fonts/cyrillic

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%version

%changelog
* Mon Jan 25 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- updating to 3.3.3.1.

* Thu Dec 17 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- fixing spec file.

* Thu Dec 03 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- separate fonts from main package,
- building RPM.
