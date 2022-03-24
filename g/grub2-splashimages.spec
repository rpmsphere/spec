Name: grub2-splashimages
Summary: a collection of great GRUB2 splashimages
Version: 1.0.1+nmu1
Release: 1
Group: admin
License: Free Software
Source0: %{name}_%{version}_all.deb
BuildArch: noarch

%description
This package contains a collection of splashimages which can be used
for GRUB2. If you'd like your splashimage in this package send them
as bug report to Debian BTS.

%prep
%setup -T -c

%build
ar -x %{SOURCE0}

%install
mkdir -p %{buildroot}
tar xf data.tar.gz -C %{buildroot}

%files
%{_datadir}/doc/%{name}
%{_datadir}/images/grub/050817-N-3488C-028.tga
%{_datadir}/images/grub/2006-02-15_Piping.tga
%{_datadir}/images/grub/Apollo_17_The_Last_Moon_Shot_Edit1.tga
%{_datadir}/images/grub/B-1B_over_the_pacific_ocean.tga
%{_datadir}/images/grub/BonsaiTridentMaple.tga
%{_datadir}/images/grub/Glasses_800_edit.tga
%{_datadir}/images/grub/Hortensia-1.tga
%{_datadir}/images/grub/Lake_mapourika_NZ.tga
%{_datadir}/images/grub/Moraine_Lake_17092005.tga
%{_datadir}/images/grub/Plasma-lamp.tga
%{_datadir}/images/grub/TulipStair_QueensHouse_Greenwich.tga
%{_datadir}/images/grub/Windbuchencom.tga

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1+nmu1
- Rebuilt for Fedora
