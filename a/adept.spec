%undefine _debugsource_packages
%global _name Adept

Summary: The Adept Programming Language
Name: adept
Version: 2.6
Release: 1
License: GPL-3.0
Group: Development/Language
URL: https://github.com/AdeptLanguage/Adept
Source0: https://github.com/AdeptLanguage/Adept/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Source1: https://github.com/AdeptLanguage/AdeptImport/archive/refs/heads/master.zip#/AdeptImport-master.zip
BuildRequires: llvm-devel
BuildRequires: openldap-devel
BuildRequires: libcurl-devel

%description
A blazing fast language for general purpose programming.

%prep
%setup -q -n %{_name}-%{version} -a 1

%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr
%{make_build}

%install
#{make_install}
install -Dm755 %{name} %{buildroot}%{_libexecdir}/%{name}/%{name}
install -Dm644 %{name}.config %{buildroot}%{_libexecdir}/%{name}/%{name}.config
mv AdeptImport-master %{buildroot}%{_libexecdir}/%{name}/import
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
exec %{_libexecdir}/%{name}/%{name} "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
* Sun Apr 10 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6
- Rebuilt for Fedora
