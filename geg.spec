Summary:	A program for drawing two-dimensional mathematical functions
Summary(pl):	Program do rysowania dwuwymiarowych wykresów funkcji matematycznych
Name:		geg
Version:	1.0.2
Release:	3
License:	GPL
Group:		Applications/Engineering
Source0:	http://www.infolaunch.com/~daveb/%{name}-%{version}.tar.gz
# Source0-md5:	0c3c15874eb10a0463dc12e680b38081
Patch0:		%{name}-etc_dir.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
URL:		http://www.infolaunch.com/~daveb/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


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
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
