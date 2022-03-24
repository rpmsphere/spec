Summary: The Dern Programming Language
Name: dern
Version: 0.489.6
Release: 1
License: Apache v2
Group: Development/Language
URL: https://octaspire.io/dern/
Source0: https://github.com/octaspire/dern/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
A platform independent programming language in standard C99. It is a dialect of
Lisp with influences from Scheme, Emacs Lisp and C. Runs in Amiga, Haiku, Plan9,
Unix, Windows and almost anything between.

%prep
%setup -q
sed -i 's|sys/sysctl.h|linux/sysctl.h|' release/plugins/external/chipmunk/src/cpHastySpace.c

%build
cd release
how-to-build/linux.sh

%install
cd release
install -d %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_bindir}
cp -a octaspire-dern-repl *.so %{buildroot}%{_libexecdir}/%{name}
ln -s ../libexec/%{name}/octaspire-dern-repl %{buildroot}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc release/LICENSE release/README
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
* Sun Sep 26 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.489.6
- Rebuilt for Fedora