Summary:	XFree86 Fonts
Summary(pl):	Fonty dla systemu XFree86 
Name:		XFree86-fonts
Version:	4.0
Release:	0.1
Copyright:	MIT
Group:		X11/XFree86
Group(pl):	X11/XFree86
Source:		ftp://ftp.xfree86.org/pub/XFree86/4.0/source/X400src-2.tgz
BuildRequires:	XFree86-devel = %{version}
Requires:	type1inst
Prereq:		%{_bindir}/mkfontdir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_fontdir	/usr/share/fonts
%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man
%define		_appnkldir	%{_datadir}/applnk

%description
This package contains the basic fonts. This package is required when you
have installed X server.

%description -l pl
Pakiet ten zawiera podstawowe czcionki. Pakiet ten jest koniecznie potrzebny,
je¶li masz zainstalowany jakikolwiek X serwer.

%package -n XFree86-75dpi-fonts
Summary:	X11R6 75dpi fonts - only need on server side
Summary(de):	X11RT 76 dpi-Fonts - nur auf Serverseite erforderlich
Summary(fr):	Fontes 75 dpi X11R6 - nécessaire uniquement côté serveur
Summary(pl):	Fonty o rozdzielczo¶ci 75dpi-niebêdne dla serwera.
Summary(tr):	X11R6 75dpi yazýtipleri - yalnýzca sunucu tarafýnda gerekir
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%ifarch sparc
Obsoletes: X11R6.1-75dpi-fonts
%endif

%description -n XFree86-75dpi-fonts
The 75dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l de -n XFree86-75dpi-fonts
Die 75dpi-Fonts, die auf meisten Linux-Systemen verwendet werden. Für Benutzer
mit einer hochauflösender Darstellung sind die 100dpi-Fonts eines getrennt
erhältlichen Pakets besser geeignet.

%description -l fr -n XFree86-75dpi-fonts
Fontes 75 dpi utilisées sur la plupart des systèmes Linux. Ceux qui ont
des écrans à haute résolution préfèreront les fontes 100 dpi disponibles
dans un autre paquetage.

%description -l pl -n XFree86-75dpi-fonts
Pakiet ten zawiera czcionki rastrowe 75dpi. W wypadku wiêkszej rozdzielczo¶ci
zalecane s± czcionki 100dpi, które s± dostêpne w osobnym pakiecie.

%description -l tr -n XFree86-75dpi-fonts
Çoðu Linux sisteminde 75dpi yazýtipi kullanýlýr. Yüksek çözünürlük kullanan
kullanýcýlar 100dpi yazýtiplerini yeðleyebilirler.

%package -n XFree86-100dpi-fonts
Summary:	X11R6 100dpi fonts - only need on server side
Summary(de):	X11R6 100dpi-Fonts - nur auf Server-Seite erforderlich
Summary(fr):	Fontes 100ppp pour X11R6 - nécessaires seulement coté serveur.
Summary(pl):	Fonty o rozdzielczosci 100dpi-niezbêdne dla serwera.
Summary(tr):	X11R6 100dpi yazýtipleri - yalnýzca sunucu tarafýnda gereklidir
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%ifarch sparc
Obsoletes: X11R6.1-100dpi-fonts
%endif

%description -n XFree86-100dpi-fonts
The 100dpi fonts used on most Linux systems. Users with high resolution
displays may prefer the 100dpi fonts available in a separate package.

%description -l de -n XFree86-100dpi-fonts
Die 100dpi-Schriftarten, die auf den meisten Linux-Systemen zum Einsatz
kommen. Anwender mit hochauflösenden Monitoren ziehen unter Umständen
die 100dpi-Schriften vor, die in einem separaten Paket erhältlich sind.

%description -l fr -n XFree86-100dpi-fonts
Les fontes 100dpi sont utilisées par la plupart des systèmes Linux.
Les utilisateurs ayant des hautes résolutions peuvent préférer les 
fontes 100dpi disponibles dans un package séparé.

%description -l pl -n XFree86-100dpi-fonts
Pakiet ten zawiera czcionki rastrowe 100dpi. Bed± one potrzebne przy pracy z
du¿± rozdzielczo¶ci±.

%description -l tr -n XFree86-100dpi-fonts
Yüksek çözünürlük kullanan kullanýcýlar 100dpi yazýtiplerini 75dpi olanlara
yeðleyebilirler.

%package -n XFree86-cyrillic-fonts
Summary:	Cyrillic fonts - only need on server side
Summary(pl):	Cyrlica
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%description -n XFree86-cyrillic-fonts
Cyrillic raster fonts.

%description -l pl -n XFree86-cyrillic-fonts
Czcionki rastrowe z cyrylic±.

%package -n XFree86-latin2-100dpi-fonts
Summary:	Latin 2 100dpi fonts - only need on server side
Summary(pl):	Pliterki
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%description -n XFree86-latin2-100dpi-fonts
Latin 2 raster fonts.

%description -l pl -n XFree86-latin2-100dpi-fonts
Czcionki rastrowe ISO-8859-2.

%package -n XFree86-latin2-75dpi-fonts
Summary:	Latin 2 75dpi fonts - only need on server side
Summary(pl):	Pliterki
Group:		X11/XFree86
Group(pl):	X11/XFree86
Prereq:		%{_bindir}/mkfontdir

%description -n XFree86-latin2-75dpi-fonts
Latin 2 raster fonts.

%description -l pl -n XFree86-latin2-75dpi-fonts
Czcionki rastrowe ISO-8859-2.

%prep
%setup -q -c 

%build
cd xc/fonts
imake -DBuildFonts -DUseInstalled -I/usr/X11R6/lib/X11/config
make Makefiles
make depend
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
(cd xc/fonts;\
 make DESTDIR=$RPM_BUILD_ROOT install;\
 make DESTDIR=$RPM_BUILD_ROOT install.man;\
)

# make TrueType font dir, touch default .dir and .scale files
install	-d $RPM_BUILD_ROOT%{_fontdir}/TTF
echo 0 > $RPM_BUILD_ROOT%{_fontdir}/TTF/fonts.dir
echo 0 > $RPM_BUILD_ROOT%{_fontdir}/TTF/fonts.scale

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_fontdir}/misc
%{_bindir}/mkfontdir

%postun
cd %{_fontdir}/misc
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-75dpi-fonts
cd %{_fontdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%postun -n XFree86-75dpi-fonts
cd %{_fontdir}/75dpi
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-100dpi-fonts
cd %{_fontdir}/100dpi
%{_bindir}/mkfontdir

%postun -n XFree86-100dpi-fonts
cd %{_fontdir}/100dpi
umask 022
%{_bindir}/mkfontdir

%post -n XFree86-cyrillic-fonts
cd %{_fontdir}/cyrillic
%{_bindir}/mkfontdir

%post -n XFree86-latin2-100dpi-fonts
cd %{_fontdir}/latin2/100dpi
%{_bindir}/mkfontdir

%post -n XFree86-latin2-75dpi-fonts
cd %{_fontdir}/latin2/75dpi
%{_bindir}/mkfontdir

%files
%defattr(644,root,root,755)
%{_fontdir}/PEX
%{_fontdir}/Speedo
%{_fontdir}/Type1
%{_fontdir}/CID
%{_fontdir}/TTF
%{_fontdir}/encodings
%{_fontdir}/local
%dir %{_fontdir}/misc
%{_fontdir}/misc/*gz
%verify(not mtime size md5) %{_fontdir}/misc/fonts.*

%files -n XFree86-75dpi-fonts
%defattr(644,root,root,755)
%dir %{_fontdir}/75dpi
%{_fontdir}/75dpi/*gz
%verify(not mtime size md5) %{_fontdir}/75dpi/fonts.*

%files -n XFree86-100dpi-fonts
%defattr(644,root,root,755)
%dir %{_fontdir}/100dpi
%{_fontdir}/100dpi/*gz
%verify(not mtime size md5) %{_fontdir}/100dpi/fonts.*

%files -n XFree86-cyrillic-fonts
%defattr(644,root,root,755)
%{_fontdir}/cyrillic

%files -n XFree86-latin2-100dpi-fonts
%defattr(644,root,root,755)
%{_fontdir}/latin2/100dpi

%files -n XFree86-latin2-75dpi-fonts
%defattr(644,root,root,755)
%{_fontdir}/latin2/75dpi
