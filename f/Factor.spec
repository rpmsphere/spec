%undefine _debugsource_packages
%global _name factor

Summary: A pratical stack language
Name: Factor
Version: 0.99
Release: 0.1
License: BSD
Group: Development/Languages
#Source0: http://downloads.factorcode.org/releases/%{version}/%{_name}-src-%{version}.zip
Source0: %{_name}-master.zip
Source1: https://downloads.factorcode.org/images/master/boot.unix-arm.64.image
Source2: https://downloads.factorcode.org/images/master/boot.unix-x86.64.image
URL: https://factorcode.org/
BuildRequires: gtkglext-devel
Requires: rlwrap tmux

%description
Factor is a concatenative, stack-based programming language with high-level
features including dynamic types, extensible syntax, macros, and garbage
collection.

%prep
%setup -q -n %{_name}-master

%build
#sed -i '/-m64/d' vm/Config.x86.64
make

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}%{_libexecdir}/%{name}
%ifarch aarch64
install -m644 %{SOURCE1} %{buildroot}%{_libexecdir}/%{name}/%{_name}.image
%else
install -m644 %{SOURCE2} %{buildroot}%{_libexecdir}/%{name}/%{_name}.image
%endif
cp -a basis core extra factor factor.entitlements libfactor.a libfactor-ffi-test.so misc shell.nix work %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
%{_libexecdir}/%{name}/%{_name} "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%post
%{_libexecdir}/%{name}/%{_name}

%files 
%doc README.md LICENSE.txt
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Mar 6 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.99
- Rebuilt for Fedora
