Summary:	Compilation controller
Name:		ccontrol
Version:	1.0
Release:	15.1
License:	GPL
Group:		Development/Tools
Source0:	https://ccontrol.ozlabs.org/releases/%{name}-%{version}.tar.bz2
URL:		https://ccontrol.ozlabs.org/
BuildRequires: xmlto, asciidoc, valgrind
BuildRequires: ghostscript-core, netpbm

%description
The ccontrol program takes over the roles of the compiler, linker and make,
and reads a configuration file to decide what to do before invoking them.
This is particularly useful for centralized control over commands and options,
such as enabling distcc and ccache. It is also great for controlling parallelism
and which compiler versions to use, based on the directory and make targets.

%prep
%setup -q

%build
./configure --bindir=%{_bindir} \
   --libdir=%{_libdir}/ccontrol \
   --mandir=%{_mandir} \
   --xmlto=/usr/bin/xmlto \
   --asciidoc=/usr/bin/asciidoc \
   --enable-debug \
   --disable-dietlibc \
   --disable-valgrind

%{__make}

%install
%{__make} install prefix=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_bindir}/g%{name}.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README TODO CHANGES COPYING
%{_bindir}/*
%{_mandir}/man1/*.1.*
%{_libdir}/%{name}

%changelog
* Sun Oct 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
