Summary:	XFree86 Fonts
Summary(pl):	Fonty dla systemu XFree86 
Name:		XFree86-fonts
Version:	3.3.3.1
Release:	54
Copyright:	MIT
Group:		X11/XFree86
Group(pl):	X11/XFree86
Source:		ftp.xfree86.org:/pub/XFree86/3.3.3/source/X333src-2.tgz
Patch0:		%{name}-3.3.3.1.patch.bz2
Buildroot:	/tmp/%{name}-%{version}-root

%define _fontdir        /usr/share/fonts

%description 
This package contains the basic fonts, programs and documentation for an X
workstation. It does not provide the X server which drives your video
hardware -- those are available in other package.

%description -l pl

%package -n	XFree86-75dpi-fonts
Summary:	X11R6 75dpi fonts - only need on server side
Summary(de):	X11RT 76 dpi-Fonts - nur auf Serverseite erforderlich
Summary(fr):	Fontes 75 dpi X11R6 - nécessaire uniquement côté serveur
Summary(pl):	Fonty o rozdzielczo¶ci 75dpi-niebêdne dla serwera.
Summary(tr):	X11R6 75dpi yazýtipleri - yalnýzca sunucu tarafýnda gerekir
Group:		X11/XFree86
Group(pl):	X11/XFree86

%ifarch sparc
Obsoletes: X11R6.1-75dpi-fonts
%endif

%description -n XFree86-75dpi-fonts
The 75dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%package -n	XFree86-100dpi-fonts
Summary:	X11R6 100dpi fonts - only need on server side
Summary(de):	X11R6 100dpi-Fonts - nur auf Server-Seite erforderlich
Summary(fr):	Fontes 100ppp pour X11R6 - nécessaires seulement coté serveur.
Summary(pl):	Fonty o rozdzielczosci 100dpi-niezbêdne dla serwera.
Summary(tr):	X11R6 100dpi yazýtipleri - yalnýzca sunucu tarafýnda gereklidir
Group:		X11/XFree86
Group(pl):	X11/XFree86

%ifarch sparc
Obsoletes: X11R6.1-100dpi-fonts
%endif

%description -n XFree86-100dpi-fonts
The 100dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%package -n	XFree86-cyrillic-fonts
Summary:	Cyrillic fonts - only need on server side
Summary(pl):	Cyrlica
Group:		X11/XFree86
Group(pl):	X11/XFree86

%description -n XFree86-cyrillic-fonts
The 75dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l de -n XFree86-100dpi-fonts
Die 100dpi-Schriftarten, die auf den meisten Linux-Systemen zum Einsatz
kommen. Anwender mit hochauflösenden Monitoren ziehen unter Umständen
die 100dpi-Schriften vor, die in einem separaten Paket erhältlich sind.

%description -l de -n XFree86-75dpi-fonts
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. Für Benutzer
mit einer hochauflösender Darstellung sind die 100dpi-Fonts eines getrennt
erhältlichen Pakets besser geeignet.

%description -l de -n XFree86-cyrillic-fonts

%description -l fr -n XFree86-100dpi-fonts
Les fontes 100dpi sont utilisées par la plupart des systèmes Linux.
Les utilisateurs ayant des hautes résolutions peuvent préférer les 
fontes 100dpi disponibles dans un package séparé.

%description -l fr -n XFree86-75dpi-fonts
Fontes 75 dpi utilisées sur la plupart des systèmes Linux. Ceux qui ont
des écrans à haute résolution préfèreront les fontes 100 dpi disponibles
dans un autre paquetage.

%description -l fr -n XFree86-cyrillic-fonts

%description -l tr -n XFree86-100dpi-fonts
Yüksek çözünürlük kullanan kullanýcýlar 100dpi yazýtiplerini 75dpi olanlara
yeðleyebilirler.

%description -l tr -n XFree86-75dpi-fonts
Çoðu Linux sisteminde 75dpi yazýtipi kullanýlýr. Yüksek çözünürlük kullanan
kullanýcýlar 100dpi yazýtiplerini yeðleyebilirler.

%description -l tr -n XFree86-cyrillic-fonts

%description -l pl -n XFree86-75dpi-fonts
75dpi - Podstawowe czcionki dla wielu maszyn Linuxowych.
W wypadku wiêkszej rozdzielczo¶ci zalecane czcionki 100dpi s± dostêpne 
w osobnym sk³adzie.
 
%description -l pl -n XFree86-100dpi-fonts
100dpi - Podstawowe czcionki dla maszyn Linuxowych pracuj±cych z wysok±
rozdzielczo¶ci± obrazu.

%description -l pl -n XFree86-cyrillic-fonts
Cyrlica.

%prep
%setup -q -c 
%patch0 -p1

%build
# Clean up to save a *lot* of disk space
find . -name "*.orig" -print | xargs rm -f
find . -size 0 -print | xargs rm -f

cd xc/fonts
xmkmf
make Makefiles
make depend
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
(cd xc/fonts;\
 make DESTDIR=$RPM_BUILD_ROOT install;\
 make DESTDIR=$RPM_BUILD_ROOT install.man;\
)

%clean
rm -rf $RPM_BUILD_ROOT

%files -n XFree86-fonts
%defattr(644,root,root,755)
/usr/X11R6/lib/X11/fonts/PEX
/usr/X11R6/lib/X11/fonts/Speedo
/usr/X11R6/lib/X11/fonts/Type1
/usr/X11R6/lib/X11/fonts/misc

%files -n XFree86-75dpi-fonts
%defattr(644,root,root,755)
/usr/X11R6/lib/X11/fonts/75dpi

%files -n XFree86-100dpi-fonts
%defattr(644,root,root,755)
/usr/X11R6/lib/X11/fonts/100dpi

%files -n XFree86-cyrillic-fonts
%defattr(644,root,root,755)
/usr/X11R6/lib/X11/fonts/cyrillic

%changelog
* Fri Feb 12 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [3.3.3.1-4d]
- added Group(pl),
- another modifications.

* Fri Dec 18 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [3.3.3-1d]
- major changes && build for PLD

       -- sorry this spec is not finished yet but... --  

* Thu Dec 03 1998 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
- separate fonts from main package,
- building RPM.
