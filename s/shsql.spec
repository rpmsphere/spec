Name:         shsql
Summary:      Shell SQL RDBMS
URL:          http://quisp.sourceforge.net/sqlman/html/shsql_home.html
Group:        Database
License:      GPL
Version:      1.28
Release:      4.1
Source0:      http://quisp.sourceforge.net/download/quisp128.tar.gz

%description
SHSQL is a standalone SQL database that stores data in ASCII
text files. It has a small memory footprint and code size and
can be embedded directly into applications -- there is no server
process. SHSQL is a pared-down SQL implementation but retains useful
features such as timeout record locking and search engine comparison
operators. A SHSQL database can be updated via SQL, or by editing
data files with a text editor. Applications link to the supplied "C"
language API. There is also a command-line SQL utility.

%prep
%setup -q -n quisp128

%build
cd sqlsrc
%{__make} %{_smp_mflags} \
      CC="%{__cc}" CFLAGS="%{optflags -O} -DSHSQL"
cd ..
mv bin/newproject.sh shsql_newproject

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_libdir} \
    $RPM_BUILD_ROOT%{_mandir}/man1
install -c -m 755 \
    shsql_newproject $RPM_BUILD_ROOT%{_bindir}
install -c -m 755 \
    bin/* $RPM_BUILD_ROOT%{_bindir}
install -c -m 644 \
    lib/* $RPM_BUILD_ROOT%{_libdir}
install -c -m 644 \
    sqlman/manshsql/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/*
%{_libdir}/lib*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.28
- Rebuild for Fedora
