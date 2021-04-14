%undefine _debugsource_packages

Summary: Schlampisoft X-Window Workbench
Name: xwb
Version: 3.1
Release: 6.2
Source0: http://www.schlampisoft.de/software/download/%{name}-%{version}.tgz
License: GPL
URL: http://www.schlampisoft.de/software/index.en.html
Group: Development/Tools
BuildRequires: libX11-devel
BuildRequires: xview-devel

%description
Tool for editing source files of any programming language and text processor.
Behaviour for compiling and executing the target file is set up individually
by recognizing the file name extension. Any type of file type characterisation
can be added.

%prep
%setup -q
sed -i -e 's| -R| -L|' -e 's|-I$(HEADER_DEST)|-I$(HEADER_DEST) -I/usr/include/tirpc|' -e 's| -lX11| -lX11 -ltirpc|' Makefile
sed -i -e 's|union wait|int|' -e 's|status->w_retcode|*status|' xwb.c

%build
make

%install
rm -rf %{buildroot}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.config %{buildroot}/usr/openwin/lib/system.xwbrc

%clean
rm -rf %{buildroot}

%files
%doc xwb.README
%{_bindir}/%{name}
/usr/openwin/lib/system.xwbrc

%changelog
* Sun Apr 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1
- Rebuilt for Fedora
