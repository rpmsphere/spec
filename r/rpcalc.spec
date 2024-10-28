Name:           rpcalc
Version:        0.8.2
Release:        1
Summary:        A simple RPN (Reverse Polish Notation) calculator
Group:          Applications/System
License:        GPLv2
URL:            https://rpcalc.bellz.org/
Source0:        https://prdownload.berlios.de/rpcalc/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-qt5-devel
Requires:       python3-qt5

%description
rpCalc is a simple RPN (Reverse Polish Notation) calculator for X.
It works much like an HP calculator, and all of the commands can be
entered using the keyboard or a mouse.
rpCalc is based on the PyQt library.

%prep
%setup -q -n rpCalc

%build

%install
rm -rf $RPM_BUILD_ROOT
python3 install.py -p /usr -i %{_datadir}/pixmaps -b $RPM_BUILD_ROOT
 
%files
%doc doc/INSTALL doc/LICENSE doc/README.html
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon May 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.2
- Rebuilt for Fedora
* Wed Aug 12 2009 Paulo Roma <roma@lcg.ufrj.br> 0.6.0-1
- Initial build
