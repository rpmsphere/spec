Name:           electrum
Version:        1.7.3
Release:        4.1
License:        GPL-3.0
Summary:        Lightweight Bitcoin Client
URL:            http://electrum.ecdsa.org/
Group:          Productivity/Networking/Other
Source:         http://electrum.bitcoin.cz/download/Electrum-%{version}.tar.gz
Patch0:         %{name}-desktop.patch
BuildRequires:  python-devel
BuildRequires:  PyQt4-devel
Requires:       python-ecdsa
Requires:       python-slowaes
Requires:       PyQt4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Electrum is an easy to use Bitcoin client. It protects you from losing
coins in a backup mistake or computer failure, because your wallet can
be recovered from a secret phrase that you can write on paper or learn
by heart. There is no waiting time when you start the client, because
it does not download the Bitcoin blockchain.

%prep
%setup -q -n Electrum-%{version}
%patch0

%build
pyrcc4 icons.qrc -o lib/icons_rc.py
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

mkdir -p  %{buildroot}%{_datadir}/pixmaps/
mv %{buildroot}%{_datadir}/app-install/icons/electrum.png %{buildroot}%{_datadir}/pixmaps/electrum.png
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/electrum
%{_datadir}/electrum/
%{_datadir}/pixmaps/electrum.png
%{_datadir}/applications/electrum.desktop
%{python_sitelib}/*

%changelog
* Sat Apr 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.3
- Rebuilt for Fedora
* Wed Apr 17 2013 prusnak@opensuse.org
- updated to 1.7.3
* Tue Mar 26 2013 prusnak@opensuse.org
- updated to 1.7.2
* Thu Mar 21 2013 prusnak@opensuse.org
- updated to 1.7.1
* Sun Mar 17 2013 prusnak@opensuse.org
- updated to 1.7
* Mon Feb 18 2013 prusnak@opensuse.org
- updated to 1.6.2
* Fri Dec 21 2012 prusnak@opensuse.org
- updated to 1.5.7
* Fri Dec 14 2012 prusnak@opensuse.org
- created package (version 1.5.6)
