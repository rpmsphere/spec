Name:           mandelbulber
Version:        1.21
Release:        8.1
Summary:        Advanced 3D fractal generator
License:        GPLv3
URL:            http://www.mandelbulber.com/
Source0:        http://download.sourceforge.net/project/mandelbulber/%{name}%{version}-1.orig.tar.gz
Source1:        http://www.boost.org/LICENSE_1_0.txt
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  mesa-libOpenCL llvm-libs
BuildRequires:  ocl-icd-devel

%description
Mandelbulber is an experimental application that helps to make rendering 3D 
Mandelbrot fractals much more accessible. A few of the supported 3D fractals: 
Mandelbulb, Mandelbox, BulbBox, JuliaBulb, Menger Sponge, Quaternion, 
Trigonometric, Hypercomplex, and Iterated Function Systems (IFS). All of these
can be combined into infinite variations with the ability to hybridize 
different formulas together. 

** FEATURES **
* GUI created in the GTK+ 2 environment.
* Multi-core rendering.
* 3D Navigator with tools to see how close the camera is to the fractal 
surface.
* Complex 3D shading: hard shadows, 3 modes of ambient occlusion, depth of 
field, reflections, fog, glow, primitive objects, and water.
* Lights can be manually or randomly placed. Volumetric lighting available.
* Camera animation: Keyframe and mouse controlled flight.
* Keyframe animation of all parameters.
* Camera lenses: three-point projection, fisheye, and equirectangular 
projection.
* Distance estimation algorithm to reduce render times and artifacts of ray 
marching.
* Low memory mode to render images larger than 16,000 x 16,000 pixels.
* OpenCL support.

%prep
%setup -qn %{name}%{version}-1.orig
cp -p %{SOURCE1} .

%build
make CXXFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}" -C makefiles all

%install
# Install data files.
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pa usr/share/* %{buildroot}%{_datadir}/%{name}/

# Install binary.
mkdir -p %{buildroot}%{_bindir}
install -pDm755 makefiles/%{name} %{buildroot}%{_bindir}/%{name}

# Install the desktop file.
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: buddhi1980@gmail.com
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">mandelbulber.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>View 3D Mandelbrot fractals</summary>
  <description>
    <p>
      Mandelbulber is an application for generating, rendering and viewing
      3D Mandelbrot fractals.
      It supports the generation of many different 3D Fractals, including
      Mandelbulb, Menger Sponge, BulbBox, Quaternion and Hypercomplex fractal
      systems.
      It has an extensive user interface for tweaking the variables of your
      fractals, and then renders your fractal in a seperate window where you can
      pan and zoom in on your mathmatical creation.
      Mandelbulber also has the ability to specify a camera, camerapath and
      keyframes to render a fly-through style video of your fractal creation.
    </p>
  </description>
  <url type="homepage">http://www.mandelbulber.com/</url>
  <screenshots>
    <screenshot type="default">http://www.mandelbulber.com/main_theme/random/screenshot_HR.jpg</screenshot>
  </screenshots>
</application>
EOF

%files
%doc COPYING LICENSE_1_0.txt NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Apr 25 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.21
- Rebuilt for Fedora
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.21-5
- Rebuilt for GCC 5 C++11 ABI change
* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.21-4
- Add an AppData file for the software center
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Tue May 20 2014 Christopher Meng <rpm@cicku.me> - 1.21-2
- Include Boost software license.
* Sat Feb 15 2014 Christopher Meng <rpm@cicku.me> - 1.21-1
- Update to 1.21
* Sun Jul 15 2012 Christopher Meng <rpm@cicku.me> - 1.12-1
- Initial Package
