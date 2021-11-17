Name:         seed7
Summary:      Seed7 Programming Language
URL:          http://seed7.sourceforge.net/
Group:        Development/Language
License:      LGPL
Version:      05.20210904
Release:      1
Source0:      http://downloads.sourceforge.net/project/seed7/seed7/seed7_%(echo %{version}|tr . _)/seed7_%(echo %{version}|tr . _).tgz
BuildRequires: libX11-devel
BuildRequires: ncurses-devel
BuildRequires: postgresql-server-devel
BuildRequires: firebird-devel
BuildRequires: mariadb-devel
Requires: libX11, ncurses, gcc, glibc-devel

%description
Seed7 is an extensible general purpose programming language. It is
a higher level language compared to Ada, C/C++ and Java. Its major
features include: user defined statements and operators, abstract
data types, templates without special syntax, OO with interfaces and
multiple dispatch, statically typed, interpreted or compiled, and
portability.

%prep
%setup -q -n seed7
sed -i '71i #undef sprintf\n#undef snprintf' src/sql_post.c

%build
export ADDITIONAL_SYSTEM_LIBS="-lmysqlclient -lsqlite3 -lpq -lodbc -lX11 -lreadline -lncurses -lfbclient" INCLUDE_OPTIONS="-I/usr/include/pgsql -I/usr/include/pgsql/server"
make -C src S7_LIB_DIR=%{_libdir}/seed7/bin SEED7_LIBRARY=%{_libdir}/seed7/lib depend s7 s7c
rm prg/s7 prg/s7c
mv prg examples

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 bin/s7 $RPM_BUILD_ROOT%{_bindir}/s7
install -m 755 bin/s7c $RPM_BUILD_ROOT%{_bindir}/s7c
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/seed7/lib
install -m 644 lib/*.s7i $RPM_BUILD_ROOT%{_libdir}/seed7/lib
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/seed7/bin
install -m 644 bin/*.a $RPM_BUILD_ROOT%{_libdir}/seed7/bin

%files
%doc COPYING LGPL doc/* examples
%{_bindir}/s7*
%{_libdir}/seed7

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 05.20210904
- Rebuilt for Fedora
