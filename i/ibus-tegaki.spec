Name:           ibus-tegaki
Version:        0.3.1
Release:        6.1
Summary:        The Tegaki engine for IBus platform
Group:          System/I18n/Japanese
License:        GPLv2+
URL:            https://tegaki.org/
Source0:        https://github.com/tegaki/tegaki/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         install_dir.diff
BuildArch:      noarch
BuildRequires:  python2-devel, pkgconfig, intltool
Requires:       ibus, tegaki-pygtk

%description
The Tegaki engine for IBus platform.

%prep
%setup -q
%patch 0

%build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%post
%{_bindir}/ibus write-cache --system &>/dev/null || :

%postun
%{_bindir}/ibus write-cache --system &>/dev/null || :

%files
%doc AUTHORS COPYING ChangeLog README
%{_prefix}/lib/ibus-tegaki
%{_prefix}/lib/python*/site-packages/ibus_tegaki*
%{_datadir}/ibus-tegaki
%{_datadir}/ibus/component/tegaki.xml

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
