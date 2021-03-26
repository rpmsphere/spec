Name:           tablix2
Summary:        Kernel for solving general timetabling problems
Version:        0.3.5
Release:        11.1
License:        GPL-2.0+
Group:          Productivity/Office/Management
URL:            http://www.tablix.org/
BuildRequires:  libxml2-devel
#BuildRequires:  pvm
Requires:       gnuplot
Source:         %{name}-%{version}.tar.bz2
Source1:        tablix2-bash_completion
Patch1:         tablix2-locale.patch

%description
Tablix is a powerful free software kernel implementing a parallel genetic
algorithm. It can be used to solve a large subset of discreet multivariable
optimization problems, but is specially optimized for timetabling. Because of
its modular design it is relatively simple to adapt Tablix to needs of a
specific organization.

Input and output is in form of specially formatted XML files, which can be
exported to a variety of formats including HTML for publishing on the web and
Comma-separated values suitable for import into other applications and further
processing. New formats can be added by writing custom export modules.

Author:
-------
Tomaž Šolc 

%package devel
Summary:        Development files for tablix2
Group:          Development/Libraries/Other
Requires:       %name = %version
Requires:       libxml2-devel
#Requires:       pvm

%description devel
This package contains header files necessary for building additional Tablix
modules.

Tablix is a powerful free software kernel implementing a parallel genetic
algorithm. It can be used to solve a large subset of discreet multivariable
optimization problems, but is specially optimized for timetabling. Because of
its modular design it is relatively simple to adapt Tablix to needs of a
specific organization.

Input and output is in form of specially formatted XML files, which can be
exported to a variety of formats including HTML for publishing on the web and
Comma-separated values suitable for import into other applications and further
processing. New formats can be added by writing custom export modules.

Author:
-------
Tomaž Šolc

%package doc
Summary:        Tablix User Manual
Group:          Documentation/Other
Requires:       %name = %version
BuildArch:      noarch

%description doc
This package contains Tablix User's Manual, Tablix modules HOW-TO, Modules
reference documentation and Tablix kernel API reference.

Tablix is a powerful free software kernel implementing a parallel genetic
algorithm. It can be used to solve a large subset of discreet multivariable
optimization problems, but is specially optimized for timetabling. Because of
its modular design it is relatively simple to adapt Tablix to needs of a
specific organization.

Input and output is in form of specially formatted XML files, which can be
exported to a variety of formats including HTML for publishing on the web and
Comma-separated values suitable for import into other applications and further
processing. New formats can be added by writing custom export modules.

Author:
-------
Tomaž Šolc

%prep
%setup -q
%patch1 -p1

%build
%configure --disable-static \
       --enable-conv \
       --disable-rpath
#       --with-pvm3 

%__make %{?jobs:-j%jobs}

%install
%makeinstall
mkdir -p %{buildroot}%{_includedir}/%{name}
install -m644 src/*.h %{buildroot}%{_includedir}/%{name}/
install -Dm644 %{S:1} %{buildroot}/%{_sysconfdir}/bash_completion.d/%name
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %name.lang
%doc AUTHORS BUGS README COPYING ChangeLog NEWS
%doc examples/*.xml
%doc examples/*.dtd
%doc examples/*.css
%doc %{_mandir}/man1/*
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%config %{_sysconfdir}/bash_completion.d/%name
%{_bindir}/%{name}*
%{_libdir}/%{name}/*
%{_datadir}/%{name}/*

%files devel
%doc examples/modules/*
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%files doc
%doc doc/*.pdf
%doc doc/modules doc/doxygen

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.5
- Rebuild for Fedora
* Mon Jan 19 2009 lars@linux-schulserver.de
- added bash completion file
* Thu Jan 15 2009 lars@linux-schulserver.de
- initial version 0.3.5
