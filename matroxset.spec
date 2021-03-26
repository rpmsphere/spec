%global debug_package %{nil}

Name:           matroxset
Version:        0.4
Release:        4.1
License:        GPL
Group:          System
Summary:        Configure the Matrox Framebuffer
Source:         %{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel

%description
matroxset is a program to manipulate the Matrox card directly. It allows you
to re-connect internal CRT devices to external heads, and set the output type
of the CRT's.

%prep
%setup -q

%build
CFLAGS=$RPM_OPT_FLAGS make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 matroxset normal swapit swapped $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
