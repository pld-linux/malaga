Summary:	Malaga - a Natural Language Analysis System
Summary(pl.UTF-8):	Malaga - system analizy języków naturalnych
Name:		malaga
Version:	7.12
Release:	6
License:	GPL v2+
Group:		Libraries
Source0:	http://home.arcor.de/bjoern-beutel/malaga/%{name}-%{version}.tgz
# Source0-md5:	873b292d923e2d1c0643769aa58c1882
Patch0:		%{name}-info.patch
Patch1:		%{name}-verbose.patch
Patch2:		link.patch
URL:		http://home.arcor.de/bjoern-beutel/malaga/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Malaga is a software package for the development and application of
grammars that are used for the analysis of words and sentences of
natural languages. It is a language-independent system that offers a
programming language for the modelling of the language-dependent
grammatical information. This language is also called Malaga.

Malaga is based on the grammatical theory of the "Left Associative
Grammar" (LAG), developed by Roland Hausser, professor for Computational
Linguistics at University of Erlangen, Germany.

%description -l pl.UTF-8
Malaga to pakiet do programowania i stosowania gramatyk używawnych
przy analizie słów i zdań w językach naturalnych. Jest to system
niezależny od języka, oferujący język programowania do modelowania
informacji gramatycznych zależnych od języka. Ten język programowania
także nazywa się Malaga.

Malaga jest oparta na teorii gramatycznej LAG (Left Associative
Grammar - gramatyka wiązana lewostronnie), opracowanej przez Rolanda
Haussera, profesora lingwistyki obliczeniowej na uniwersytecie w
Erlagen w Niemczech.

%package devel
Summary:	Header files for Malaga library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Malaga
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0

%description devel
Header files for Malaga library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Malaga.

%package static
Summary:	Static Malaga library
Summary(pl.UTF-8):	Statyczna biblioteka Malaga
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Malaga library.

%description static -l pl.UTF-8
Statyczna biblioteka Malaga.

%package gtk
Summary:	GUI to display Malaga results or debugging states
Summary(pl.UTF-8):	Graficzny interfejs wyświetlający wyniki i stany diagnostyczne Malagi
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2 >= 2:2.8

%description gtk
GUI to display Malaga results or debugging states.

%description gtk -l pl.UTF-8
Graficzny interfejs wyświetlający wyniki i stany diagnostyczne Malagi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_INFO=true

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{_bindir}/malaga
%attr(755,root,root) %{_bindir}/mallex
%attr(755,root,root) %{_bindir}/malmake
%attr(755,root,root) %{_bindir}/malrul
%attr(755,root,root) %{_bindir}/malsym
%attr(755,root,root) %{_libdir}/libmalaga.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmalaga.so.7
%{_datadir}/malaga
%{_mandir}/man1/malaga.1*
%{_mandir}/man1/mallex.1*
%{_mandir}/man1/malmake.1*
%{_mandir}/man1/malrul.1*
%{_mandir}/man1/malsym.1*
%{_infodir}/malaga.info*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmalaga.so
%{_libdir}/libmalaga.la
%{_includedir}/malaga.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmalaga.a

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/malshow
%{_mandir}/man1/malshow.1*
