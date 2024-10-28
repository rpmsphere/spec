Summary:        A powerful open source data analysis software
Name:           scicraft
Version:        1.0.2
Release:        9.1
License:        GPLv2
Group:          Sciences/Other
URL:            https://www.scicraft.org/
Source0:        https://www.scicraft.org/files/%{name}-ng_%{version}.tar.bz2
BuildRequires:  python2-devel
BuildRequires:  texlive-dvipdfmx
BuildRequires:  latex2html
BuildRequires:  perl
BuildRequires:  ImageMagick
BuildRequires:  dos2unix
Requires:       python2
Requires:       python-qwt
Requires:       octave 
Requires:       python-vtk
Requires:       python-rpy pygtk2.0-libglade python-gobject gnome-python python-matplotlib python-scipy
Requires:       R-base
BuildArch:      noarch

%description
SciCraft is a powerful open source data analysis software with an easy-to-use
graphical user interface.

Many of todays scientists face the following problem: They need to integrate a
substantial number of computational tools to solve problems. 

SciCraft is a software designed to make software and method integration easier.
It is also designed to make different computational tools easily available to
the user. In theory SciCraft can be used to integrate any type of software, but
we have in particular focused on the integration and availability of data
analysis methods which originate from fields such as bioinformatics,
statistics, chemometrics and artificial intelligence. One reason for this focus
is that irrespective of the scientific field in question, there is almost
always a need to perform data analysis.

%prep
%setup -qn %{name}-ng-%{version}
# %patch 0
#find -type f -exec dos2unix -U {} \;
mkdir -p .svn

%build

%install
rm -rf %buildroot
%make_install

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%attr(0755, root, root) %{_bindir}/*
%{_prefix}/lib/*
%{_datadir}/doc/%{name}-ng

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.2-6mdv2010.0
+ Revision: 442818
- rebuild
* Tue Mar 17 2009 Frederic Crozat <fcrozat@mandriva.com> 1.0.2-5mdv2009.1
+ Revision: 356633
- Replace old broken gnome1 dependencies with gnome2 ones
  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.2-3mdv2009.0
+ Revision: 252052
- rebuild
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Fri Dec 21 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.2-1mdv2008.1
+ Revision: 136282
- fix build with new version
- add some requires
- fix build
- create directory
- kill re-definition of %%buildroot on Pixel's request
  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version
    - spec file clean
* Tue May 09 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.18.0-2mdk
- Fix BuildRequires
* Mon May 08 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.18.0-1mdk
- 0.18.0
- add examples package
* Tue Aug 09 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.15.0-1mdk
- initial contrib
