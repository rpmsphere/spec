Name: screenkey
Version: 1.1
Release: 1
Summary: A screen-cast tool to show your keys and based on key-mon project
Group: Video
License: GPL+
URL: https://launchpad.net/screenkey
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar.gz
BuildRequires: python2-devel
BuildRequires: python2-distutils-extra
BuildArch: noarch

%description
A screen-cast tool to show your keys inspired by Screenflick and based on
the key-mon project.

%prep
%setup -q
sed -i 's/^Categories=.*/Categories=AudioVideo;Video;Recorder;/' data/screenkey.desktop
sed -i '/^Version=/d' data/screenkey.desktop

%build
%py2_build

%install
mkdir -p %buildroot%_docdir/%name-%version
find build/lib* -name '*.py' -exec sed -i "1{/^#!/d}" {} \; && \
%py2_install

%files
%doc %{_docdir}/%{name}
%_bindir/screenkey
%_datadir/applications/screenkey.desktop
%python2_sitelib/Screenkey
%exclude %python2_sitelib/*.egg-info

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- %%name.desktop fixes
* Wed Sep 04 2013 Denis Smirnov <mithraen@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
