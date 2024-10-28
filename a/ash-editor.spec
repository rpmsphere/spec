Summary: A modern terminal text editor
Name: ash-editor
Version: 0.1.0.dev14
Release: 1
License: GPL-2.0
Group: Development/Languages
Source0: https://github.com/akashnag/ash/raw/dev/dist/%{name}-%{version}.tar.gz
URL: https://github.com/akashnag/ash
BuildArch: noarch

%description
ash is a simple and clean terminal-based text editor, that aims to be easy to use
with modern key-bindings. It is capable of handling multiple files simultaneously
and has a wide array of modern features.

%prep
%setup -q

%build
%py3_build

%install
%py3_install
mv %{buildroot}%{_bindir}/ash %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
mv %{buildroot}/usr/assets %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}/usr/docs

%files 
%doc *.md
%{_bindir}/%{name}
%{python3_sitelib}/ash*
%{_datadir}/%{name}

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0.dev14
- Rebuilt for Fedora
