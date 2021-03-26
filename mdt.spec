Name:           mdt
BuildRequires:  nasm
BuildRequires:  libx86emu-devel
License:        GPL v3 or later
Group:          System/Hardware
Summary:        Video BIOS monitor detection tool 
Version:        1.6
Release:        1
Source:         %{name}-master.zip
URL:            https://github.com/wfeldt/mdt

%description
This is a tiny program that can be run either directly or from DOS and uses
VESA BIOS functions to read monitor data. The basic purpose is to see
whether this works correctly.

%prep
%setup -q -n %{name}-master

%build
make mdt

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%doc README* Changelog COPYING

%changelog
* Fri Feb 14 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuild for Fedora
