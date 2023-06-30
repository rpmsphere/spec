Summary:       Scientific calculator (GTK+)
Name:          calcoo
Version:       1.3.18
Release:       9.1
License:     GPL
URL:           https://calcoo.sourceforge.net
Group:         Applications/Utilities
Source:        https://prdownloads.sourceforge.net/calcoo/%{name}-%{version}.tar.gz
BuildRequires: libpng-devel
BuildRequires: gtk2-devel

%description
Calcoo is a scientific calculator designed to provide maximum usability. 
The features that make Calcoo better than (at least some) other calculator 
programs are:

  * bitmapped button labels and display digits to improve readability
  * no double-function buttons - you need to click only one button
    for any operation (except for arc-hyp trigonometric functions)
  * undo/redo buttons
  * both RPN (reverse Polish notation) and algebraic modes
  * copy/paste interaction with X clipboard
  * display tick marks to separate thousands
  * two memory registers with displays
  * displays for Y, Z, and T registers

%prep
%setup -q

%build
export LDFLAGS=-lm
%configure
make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc ChangeLog INSTALL COPYING README
%{_bindir}/calcoo
%{_mandir}/man1/calcoo.1*

%changelog
* Tue May 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.18
- Rebuilt for Fedora

* Tue Sep 16 2003 Alexei Kaminski <kaminski@tpi.umn.edu>
  - New upstream release
