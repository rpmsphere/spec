%undefine _debugsource_packages

Name: miranda
Summary: A non-strict polymorphic functional language
Version: 2.066
Release: 1
Group: Development/Language
License: BSD-like
URL: https://miranda.org.uk/
Source0: https://www.cs.kent.ac.uk/people/staff/dat/miranda/src/mira-2066-src.tgz

%description
Miranda is a pure, non-strict, polymorphic, higher order functional
programming language designed by David Turner in 1983-6. The language
was widely taken up, both for research and for teaching, and had a strong
influence on the subsequent development of the field, influencing in
particular the design of Haskell, to which it has many similarities.

%prep
%setup -q -n %{name}
sed -i 's|-w|-w -Wl,--allow-multiple-definition|' Makefile
sed -i -e 's|-m32|-D__x86_64__|' -e 's|`quotehostinfo`|`./quotehostinfo`|' Makefile
sed -i 's|/usr/bin/mira |/usr/bin/miranda |' ex/box.m ex/mrev miralib/manual/31/4 miralib/manual/32 miralib/ex/box.m miralib/ex/mrev
sed -i 's|/home/dat/mira/states/src/miranda/mira |/usr/bin/miranda |' ex/box.m miralib/ex/box.m

%build
gcc fdate.c -o fdate
make

%install
install -Dm755 mira %{buildroot}%{_bindir}/%{name}
install -Dm644 mira.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -d %{buildroot}/usr/lib
cp -a miralib %{buildroot}/usr/lib

%files
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
/usr/lib/miralib

%changelog
* Thu Feb 18 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.066
- Rebuilt for Fedora
