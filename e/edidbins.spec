Summary:	Generic monitor edid files
Name:		edidbins
Version:	1.1
Release:	7
Group:		System/Kernel and hardware
License:	LGPLv2+
URL:		https://github.com/torvalds/linux/tree/master/Documentation/EDID
BuildArch:	noarch
#The tarball for these files was generated from the cloned sources from the above url. The files were copied to a directory edidbins and then compressed with "tar -Jcvf kernel-edidbins edidbins/*" It is unlikely that these sources will change. Proprietary edid's should have their own package.
Source0:	kernel-edidbins-%{version}.tar.xz
BuildRequires:	dos2unix

%description
Provides five binary edid files to give to support kernel edid loading feature.

%prep
%autosetup -n %{name} -p1
#force gcc
sed -i 's/@cc/@gcc/' Makefile

%build
%make_build

%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/edid
cp -avf *.bin %{buildroot}%{_prefix}/lib/firmware/edid

%files
/usr/lib/firmware/edid/*.bin

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora