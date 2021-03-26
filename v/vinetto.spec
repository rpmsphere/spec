Name:           vinetto
Version:        0.07
Release:        3.1
Summary:        A forensics tool to examine Thumbs.db files
Group:          Applications/System
License:        GPLv2+
URL:            http://vinetto.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-beta-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-pillow

%description
Vinetto is a forensics tool to examine Thumbs.db files.  It is
a console program to extract thumbnail images and their metadata
from those thumbs.db files generated under Microsoft Windows.

%prep
%setup -q -n %{name}-beta-%{version}

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python2_sitelib}/vin*

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.07
- Rebuild for Fedora
* Mon Mar 22 2010 Fabian Affolter <fabian@bernewireless.net> - 0.07-1.beta
- Initial spec for Fedora
