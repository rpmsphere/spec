%undefine _debugsource_packages

Summary: The Generic Window Manager
Name: gwm
Version: 1.8d
#Version: 2.1
Release: 15.1
License: public domain
Group: X11/Window Managers
URL: https://old.koalateam.com/gwm/
Source: ftp://ftp.x.org/contrib/window_managers/gwm/gwm-%{version}.tgz
BuildRequires: imake
BuildRequires: byacc
BuildRequires: flex
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXpm-devel

%description
GWM is the "emacs" of window managers.  Developed by Colas Nahaboo as part 
of the Koala Project, GWM is very extensible, allowing the user to change 
the look and feel in a Lisp-like language called WOOL.

I have compiled GWM with the "GWM spy" (packet sent to the GWM author to track 
GWM usage) feature disabled.

%prep
%setup -q
sed -i '/libXpm.a/d' Imake*
sed -i 's|/usr/local|/usr|g' gwm.man Imakefile Makefile Makefile.noXtree Make.TEMPLATE PROBLEMS data/ImakeB data/Imakefile data/Makefile doc/*.tex contrib/scripts/find-bar-nils

%build
xmkmf
make

%install
%make_install install.man

%files
%doc doc README
%{_bindir}/gwm
/usr/lib/gwm
%{_mandir}/man1/gwm.1*

%changelog
* Thu Jun 04 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8d
- Rebuilt for Fedora
