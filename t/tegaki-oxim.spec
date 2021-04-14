%define __python /usr/bin/python2
Summary: 	Chinese and Japanese Handwriting Recognition
Name: 		tegaki-oxim
Version: 	0.2
Release: 	1
License: 	GPLv2+
Group: 		System/Internationalization
Source0: 	%name-%version.tar.gz
BuildArch:	noarch
Requires:	tegaki-pygtk
Requires:       oxim

%description
Tegaki-Oxim is an ongoing project which aims to develop a free and open-source
modern implementation of handwriting recognition software, that is suitable for
both the desktop and mobile devices, and that is designed from the ground up to
work well with Chinese.

%prep
%setup -q

%build
cp -f /usr/share/automake-*/config.guess .
./configure
DESTDIR=%{buildroot} make

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} make install

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
#%{python_sitelib}/tegaki_oxim-*.egg-info
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Fri Apr 17 2009 Wind <yc.yan@ossii.com.tw> 0.1.ossii
- Build for OSSII.
