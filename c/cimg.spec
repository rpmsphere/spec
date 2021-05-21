%define	oname CImg

Summary:	Tools for advanced image processing
Name:		cimg
Version:	1.5.6
Release:	3.1
Source0:	http://sourceforge.net/projects/cimg/files/%{oname}-%{version}.zip
License:	CeCiLLv2
Group:		Graphics/Utilities
URL:		http://sourceforge.net/projects/cimg/
BuildRequires:	libX11-devel
BuildRequires:  libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	fftw3-devel
BuildRequires:	doxygen

%description
Image manipulation tools based on the CImg library, including the
greycstoration noise reduction tool.

%package   devel
Summary:   Library for advanced image processing (development files)
Group:     Development/C++

%description devel
The CImg Library is a C++ toolkit providing simple classes and functions to
load, save, process and display images in your own C++ code. It consists
only of a single header file CImg.h that must be included in your program
source. It contains useful image processing algorithms for loading/saving,
resizing/rotating, filtering, object drawing (text, lines, faces,
ellipses, ...), etc.

Images are instanciated by a class able to represent images up to 4-dimension
wide (from 1-D scalar signals to 3-D volumes of vector-valued pixels), with
template pixel types. It depends on a minimal number of libraries: you can
compile it with only standard C libraries. No need for exotic libraries and
complex dependencies.

%prep
%setup -q -n %{oname}-%{version}

%build
pushd examples
make olinux 
popd

pushd html
doxygen -u %{oname}.doxygen
doxygen %{oname}.doxygen
popd

%install
mkdir -p %{buildroot}%{_bindir}
pushd examples
mv captcha %{buildroot}%{_bindir}
mv CImg_demo %{buildroot}%{_bindir}
mv curve_editor2d %{buildroot}%{_bindir}
mv dtmri_view3d %{buildroot}%{_bindir}
mv edge_explorer2d %{buildroot}%{_bindir}
mv fade_images %{buildroot}%{_bindir}
mv gaussian_fit1d %{buildroot}%{_bindir}
mv generate_loop_macros %{buildroot}%{_bindir}
mv hough_transform2d %{buildroot}%{_bindir}
mv image2ascii %{buildroot}%{_bindir}
mv image_registration2d %{buildroot}%{_bindir}
mv image_surface3d %{buildroot}%{_bindir}
mv jawbreaker %{buildroot}%{_bindir}
mv mcf_levelsets2d %{buildroot}%{_bindir}
mv mcf_levelsets3d %{buildroot}%{_bindir}
mv odykill %{buildroot}%{_bindir}
mv pde_heatflow2d %{buildroot}%{_bindir}
mv pde_TschumperleDeriche2d %{buildroot}%{_bindir}
mv plotter1d %{buildroot}%{_bindir}
mv radon_transform2d %{buildroot}%{_bindir}
mv scene3d %{buildroot}%{_bindir}
mv spherical_function3d %{buildroot}%{_bindir}
mv tetris %{buildroot}%{_bindir}
mv tron %{buildroot}%{_bindir}
mv tutorial %{buildroot}%{_bindir}
mv use_draw_gradient %{buildroot}%{_bindir}
mv use_nlmeans %{buildroot}%{_bindir}
mv use_RGBclass %{buildroot}%{_bindir}
mv use_skeleton %{buildroot}%{_bindir}
mv wavelet_atrous %{buildroot}%{_bindir}
popd

mkdir -p %{buildroot}%{_includedir}/%{oname}
mv plugins %{buildroot}%{_includedir}/%{oname}
mv %{oname}.h %{buildroot}%{_includedir}/%{oname}
ln -s %{oname}/%{oname}.h %{oname}.h
mv %{oname}.h %{buildroot}%{_includedir}

%files
%{_bindir}/* 

%files devel
%{_includedir}/%{oname}*
%doc html README.txt Licence_CeCILL* examples

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.6
- Rebuilt for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 1.5.2-2.mga3
+ Revision: 347754
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
  + boklm <boklm>
    - Update group: Graphics/Other -> Graphics/Utilities
* Fri Dec 07 2012 dams <dams> 1.5.2-1.mga3
+ Revision: 327875
- new version 1.5.2
- update %%group
* Sun Jul 15 2012 dams <dams> 1.5.0-1.mga3
+ Revision: 270863
- add 'X11-devel' as 'BuildRequires'
- clean specfile
- imported package cimg
