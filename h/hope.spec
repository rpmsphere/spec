%undefine _debugsource_packages

Summary: Hope programming language interpreter
Name: hope
Version: 1.0
Release: 1
License: GPLv2
Group: Development/Language
URL: https://github.com/dmbaturin/hope
Source0: https://github.com/dmbaturin/hope/archive/refs/tags/1.0.tar.gz#/%{name}-%{version}.tar.gz

%description
Hope is a lazily evaluated functional programming language developed in 1970's
by Ross Paterson. It influenced the design of other lazy languages such as
Miranda and Haskell.

This version is derived from the source that was once available from the author's home
page (http://web.archive.org/web/20110709142512/http://www.soi.city.ac.uk/~ross/Hope/).

The goal of this project is to preserve Hope in its original form, so the only changes
being made are fixes required to get it to build on modern systems.

%prep
%setup -q
sed -i 's|/usr/local|/usr|' configure src/hope.1 src/hopelib.h

%build
%configure
%make_build

%install
#make_install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}/lib %{buildroot}%{_datadir}/%{name}/lib.new %{buildroot}%{_mandir}/man1
install -m755 src/%{name} %{buildroot}%{_bindir}
install -m644 lib/*.hop %{buildroot}%{_datadir}/%{name}/lib
sed -f lib/list.sed lib/Standard.hop > %{buildroot}%{_datadir}/%{name}/lib.new/Standard.hop
install -m644 src/%{name}.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc COPYING LICENSE README*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
