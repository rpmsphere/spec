Summary:	Generic monitor edid files
Name:		edidbins
Version:	1
Release:	3.1
Group:		System/Kernel and hardware
License:	LGPLv2+
URL:		https://github.com/torvalds/linux/tree/master/Documentation/EDID
BuildArch:	noarch 
Source0:	kernel-edidbins-%{version}.1.tar.xz
BuildRequires:	binutils
BuildRequires:	dos2unix
BuildRequires:	util-linux

%description
Provides five binary edid files to give to support kernel edid loading feature.

%prep
%setup -q -n %{name}

%build
make 

%install
mkdir -p %{buildroot}/lib/firmware/edid
cp -avf *.bin %{buildroot}/lib/firmware/edid

%files
/lib/firmware/edid/*.bin

%changelog
* Tue Feb 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuild for Fedora
* Wed Apr 16 2014 Bernhard Rosenkraenzer <bero@lindev.ch> 1-1
+ Revision: b7a84de
- Clean up spec
