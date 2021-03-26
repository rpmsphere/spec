Name: spec2deb
Summary: Converting a rpm package.spec to a debian source directory
Version: 0.4
Release: 1
Group: Development/Tools
License: BSD
URL: https://bitbucket.org/guidod/spec2deb
Source0: https://bitbucket.org/guidod/spec2deb/get/%{name}-%{version}.tar.gz
BuildArch: noarch

%description
The script assumes a fairly simple rpm spec file as input. If the upstream
project follows the normal GNU-style of "configure && make && make install"
then the %%script sections don't need to name much more than that. In the
real world the packager will add and remove some files as well as shifting
files from one place to another. But that's okay for the spec2deb script as
well.

%prep
%setup -q -n guidod-spec2deb-5a2bf4c295a6

%build

%install
install -Dm755 src/%{name}/%{name}.py %{buildroot}/%{_bindir}/%{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc src/COPYING.BSD src/README.TXT
%{_bindir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
