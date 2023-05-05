%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Summary: A modern BASIC programming language
Name: purebasic
Version: 6.00
Release: 1.bin
License: freeware, demo
Group: Development/Language
URL: https://www.purebasic.com/
Source0: https://www.purebasic.com/download/purebasic2-demo_x64.tgz
ExclusiveArch: x86_64
Requires: gcc gcc-c++
Requires: qt5-qtwebkit-devel mesa-libGL-devel libgnome-devel gtk3-devel
Requires: sdl12-compat-devel openssl-devel libXxf86vm-devel webkit2gtk3-devel libcanberra-devel

%description
The key features of PureBasic are portability (Windows, Linux, OS X and
Raspberry supported with the same source code), the production of very
fast and optimized native 32-bit or 64-bit executables and, of course,
the very simple BASIC language syntax. PureBasic has been created for
the beginner and expert alike. We have put a lot of effort into its
conception to produce a fast, reliable system and friendly BASIC compiler.

Free version limitations: Code size limitation (about 800 lines).

%prep
%setup -q -n purebasic_demo

%build
#No build

%install
install -d %{buildroot}%{_libexecdir}/%{name}
cp -a * %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Icon=%{_libexecdir}/%{name}/logo.png
Name=PureBasic
Comment=%{summary}
Exec=%{name}
StartupNotify=false
Terminal=false
EOF
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
echo -e "export PUREBASIC_HOME=%{_libexecdir}/%{name}\nexport PATH=\$PATH:%{_libexecdir}/%{name}/compilers" > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
echo -e "setenv PUREBASIC_HOME %{_libexecdir}/%{name}\nsetenv PATH \$PATH:%{_libexecdir}/%{name}/compilers" > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh

%files
%doc README
%{_sysconfdir}/profile.d/%{name}.*sh
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Feb 24 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 6.00
- Initial package for Fedora
