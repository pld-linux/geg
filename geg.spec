Summary:	A program for drawing two-dimensional mathematical functions
Summary(pl):	Program do rysowania dwuwymiarowych wykresów funkcji matematycznych
Name:		geg
Version:	1.0.2
Release:	2
License:	GPL
Group:		Applications/Engineering
Group(de):	Applikationen/Ingenieurwesen
Group(pl):	Aplikacje/In¿ynierskie
Source0:	http://www.infolaunch.com/~daveb/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
URL:		http://www.infolaunch.com/~daveb/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Geg (GTK+ Equation Grapher)is a simple program which will draw
two-dimensional mathematical functions (e.g., f(x) = 3 + sin(x/2)).
Geg allows you view multiple functions simultaneously, with each
function drawn in a different color. Functions can be selectively
erased. Geg's view can be zoomed in and out on selected regions.

%description -l pl
Geg (GTK+ Equation Grapher) jest prostym programem rysuj±cym wykresy
funkcji matematycznych (np. f(x) = 3 + sin(x/2)). Geg pozwala ci na
ogl±danie wielu wykresów równocze¶nie, przy czym ka¿da funkcja jest
rysowana innym kolorem. Funkcje mog± byæ selektywnie usuwane. Widok
okreslonych regionów mo¿e byæ powiêkszany i zmniejszany.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
