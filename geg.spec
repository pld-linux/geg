Summary: A program for drawing two-dimensional mathematical functions.
Name: geg
Version: 1.0.2
Release: 1
Copyright: GPL
Group: Applications/Engineering
Source0: http://www.infolaunch.com/~daveb/geg-%{version}.tar.gz 
URL: http://www.infolaunch.com/~daveb 
BuildRoot: /var/tmp/geg-root

%description
Geg (GTK+ Equation Grapher)is a simple program which will draw
two-dimensional mathematical functions (e.g., f(x) = 3 + sin(x/2)).
Geg allows you view multiple functions simultaneously, with each
function drawn in a different color.  Functions can be selectively
erased.  Geg's view can be zoomed in and out on selected regions.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT


make prefix=$RPM_BUILD_ROOT%{_prefix} install 

strip $RPM_BUILD_ROOT%{_prefix}/bin/* || :

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root) 
%doc AUTHORS COPYING ChangeLog NEWS README
%{_prefix}/bin/*
%{_prefix}/man/*/*

%changelog 
* Wed May 10 2000 Tim Powers <timp@redhat.com>
- updated to 1.0.2
- updtaed URLs

* Mon Jan 10 2000 Tim Powers <timp@redhat.com>
- rebuilt for 6.2

* Wed Jul 14 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Mon Apr 12 1999 Michael Maher <mike@redhat.com>
- built package for 6.0

* Tue Oct 06 1998 Michael Maher <mike@redhat.com>
- updated package

* Mon Aug 10 1998 Michael Maher <mike@redhat.com>
- built package                                                  
