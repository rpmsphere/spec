%undefine _debugsource_packages

Summary:	DBase III file viewer
Name:		dbview
Version:	1.0.4
Release:	3.1
Group:		System/Utility
License:	GPL
URL:		http://www.infodrom.org/projects/dbview/
Vendor:		Martin Schulze <joey@infodrom.org>
Source:		%{name}-%{version}.tar.gz
BuildRequires:	gcc

%description
dbview is a little tool that will display dBase III files. You can also use it
to convert your old .dbf files for further use with Unix. It should also work
with dBase IV files, but this is mostly untested.

By default dbview displays the contents of a dBase III or IV database file.
This is be done by displaying both the name of the field itself and its value.
At the end of every record a newline is appended.

%prep
%setup -q

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -Dp -m0755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
%{__install} -Dp -m0644 %{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc CHANGES README dBASE db_dump.header
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuilt for Fedora
* Mon Jul 13 2009 TI_Eugene <ti.eugene@gmail.com>
- Initial build for Fedora 11
