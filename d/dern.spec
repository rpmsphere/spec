Summary: The Dern Programming Language
Name: dern
Version: 0.490.0
Release: 1
License: Apache v2
Group: Development/Language
URL: https://octaspire.io/dern/
#Source0: https://github.com/octaspire/dern/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0: %{name}-master.zip
BuildRequires: SDL2_mixer-devel SDL2_image-devel SDL2_ttf-devel

%description
A platform independent programming language in standard C99. It is a dialect of
Lisp with influences from Scheme, Emacs Lisp and C. Runs in Amiga, Haiku, Plan9,
Unix, Windows and almost anything between.

%prep
%setup -q -n %{name}-master
sed -i 's|sys/sysctl.h|linux/sysctl.h|' release/plugins/external/chipmunk/src/cpHastySpace.c

%build
cd release
how-to-build/linux.sh

%install
cd release
install -d %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_bindir}
cp -a octaspire-dern-repl *.so %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
LD_LIBRARY_PATH=%{_libexecdir}/%{name} %{_libexecdir}/%{name}/octaspire-dern-repl "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%files
%doc release/LICENSE release/README
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
* Sun Jun 26 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.490.0
- Rebuilt for Fedora
