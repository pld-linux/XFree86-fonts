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
Summary(pl): Fonty o rozdzielczo�ci 75dpi-nieb�dne dla serwera.
Summary(de): X11RT 76 dpi-Fonts - nur auf Serverseite erforderlich
Summary(fr): Fontes 75 dpi X11R6 - n�cessaire uniquement c�t� serveur
Summary(tr): X11R6 75dpi yaz�tipleri - yaln�zca sunucu taraf�nda gerekir
Prereq:      /usr/X11R6/bin/mkfontdir
%ifarch sparc
Obsoletes:   X11R6.1-75dpi-fonts
%endif

%description -n %BASENAME-75dpi-fonts
The 75dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l de -n %BASENAME-75dpi-fonts
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. F�r Benutzer
mit einer hochaufl�sender Darstellung sind die 100dpi-Fonts eines getrennt
erh�ltlichen Pakets besser geeignet.

%description -l fr -n %BASENAME-75dpi-fonts
Fontes 75 dpi utilis�es sur la plupart des syst�mes Linux. Ceux qui ont
des �crans � haute r�solution pr�f�reront les fontes 100 dpi disponibles
dans un autre paquetage.

%description -l tr -n %BASENAME-75dpi-fonts
�o�u Linux sisteminde 75dpi yaz�tipi kullan�l�r. Y�ksek ��z�n�rl�k kullanan
kullan�c�lar 100dpi yaz�tiplerini ye�leyebilirler.

%description -l pl -n %BASENAME-75dpi-fonts
75dpi - Bazowe fonty dla wielu maszyn Linuxowych.
W wypadku wi�kszej rozdzielczo�ci zaleczne fonty 100dpi dost�pne 
w oddzielnym pakiecie.

%package -n %BASENAME-100dpi-fonts
Summary:     X11R6 100dpi fonts - only need on server side
Group:       X11/XFree86/fonts
Group(pl):   X11/XFree86/Fonty
Summary(pl): Fonty o rozdzielczosci 100dpi-niezb�dne dla serwera.
Summary(de): X11R6 100dpi-Fonts - nur auf Server-Seite erforderlich
Summary(fr): Fontes 100ppp pour X11R6 - n�cessaires seulement cot� serveur.
Summary(tr): X11R6 100dpi yaz�tipleri - yaln�zca sunucu taraf�nda gereklidir
Prereq:      /usr/X11R6/bin/mkfontdir
%ifarch sparc
Obsoletes:   X11R6.1-100dpi-fonts
%endif

%description -n %BASENAME-100dpi-fonts
The 100dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l pl -n %BASENAME-100dpi-fonts
100dpi - Bazowe fonty dla maszyn Linuxowych pracuj�cych w wysokiej 
rozdzielczo�ci.

%description -l de -n %BASENAME-100dpi-fonts
Die 100dpi-Schriftarten, die auf den meisten Linux-Systemen zum Einsatz
kommen. Anwender mit hochaufl�senden Monitoren ziehen unter Umst�nden
die 100dpi-Schriften vor, die in einem separaten Paket erh�ltlich sind.

%description -l fr -n %BASENAME-100dpi-fonts
Les fontes 100dpi sont utilis�es par la plupart des syst�mes Linux.
Les utilisateurs ayant des hautes r�solutions peuvent pr�f�rer les 
fontes 100dpi disponibles dans un package s�par�.

%description -l tr -n %BASENAME-100dpi-fonts
Y�ksek ��z�n�rl�k kullanan kullan�c�lar 100dpi yaz�tiplerini 75dpi olanlara
ye�leyebilirler.

%package -n %BASENAME-cyrillic-fonts
Summary:     X11R6 cyrillic fonts - only need on server side
Summary(de): X11R6 cyrillic-Fonts - nur auf Server-Seite erforderlich
Summary(fr): Fontes cyrillic pour X11R6 - n�cessaires seulement cot� serveur.
Summary(pl): X11R6 fonty 75dpi - wymagane tylko po stronie serwera
Summary(tr): X11R6 cyrillic yaz�tipleri - yaln�zca sunucu taraf�nda gereklidir
Group:       X11/XFree86/fonts
Group(pl):   X11/XFree86/Fonty
Prereq:      /usr/X11R6/bin/mkfontdir

%description -n %BASENAME-cyrillic-fonts
The cyrillic fonts used on most Linux systems. Users with high resolution
displays may prefer the cyrillic fonts available in a separate package.

%description -l de -n %BASENAME-cyrillic-fonts
Die cyrillic-Schriftarten, die auf den meisten Linux-Systemen zum Einsatz
kommen. Anwender mit hochaufl�senden Monitoren ziehen unter Umst�nden
die cyrillic-Schriften vor, die in einem separaten Paket erh�ltlich sind.

%description -l fr -n %BASENAME-cyrillic-fonts
Les fontes cyrillic sont utilis�es par la plupart des syst�mes Linux.
Les utilisateurs ayant des hautes r�solutions peuvent pr�f�rer les 
fontes cyrillic disponibles dans un package s�par�.

%description -l tr -n %BASENAME-cyrillic-fonts
Y�ksek ��z�n�rl�k kullanan kullan�c�lar cyrillic yaz�tiplerini 75dpi olanlara
ye�leyebilirler.

%description -l pl -n %BASENAME-cyrillic-fonts
Fonty cyrylicy s� u�ywane na wi�kszo�ci system�w linuxowych.

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
* Mon Jan 25 1999 Wojciech "Sas" Ci�ciwa <cieciwa@alpha.zarz.agh.edu.pl>
- updating to 3.3.3.1.

* Thu Dec 17 1998 Wojciech "Sas" Ci�ciwa <cieciwa@alpha.zarz.agh.edu.pl>
- fixing spec file.

* Thu Dec 03 1998 Wojciech "Sas" Ci�ciwa <cieciwa@alpha.zarz.agh.edu.pl>
- separate fonts from main package,
- building RPM.
