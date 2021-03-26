%define pkgname		SweetHome3D
%define pkgmod		3DModels
%define pkgtextu	Textures
%define modelver	1.6.4
%define textuver	1.2
%define texturesver	1.6
%define furniturever	1.24

Name:		sweethome3d
Version:	6.1
Release:	%mkrel 1
Summary:	A free interior design application, with a 3D preview
License:	GPLv2
Group:		Graphics/3D
URL:		http://www.sweethome3d.com/
Source0:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-source/SweetHome3D-%{version}-src/%{pkgname}-%{version}-src.zip
Source1:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-Contributions-%{modelver}.zip
Source2:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-KatorLegaz-%{modelver}.zip
Source3:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-LucaPresidente-%{modelver}.zip
Source4:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-Reallusion-%{modelver}.zip
Source5:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-Scopia-%{modelver}.zip
Source6:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-Trees-%{modelver}.zip
Source7:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-BlendSwap-CC-BY-%{modelver}.zip
Source8:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-models/3DModels-%{modelver}/%{pkgmod}-BlendSwap-CC-0-%{modelver}.zip
Source9:	sweethome3d_128x128.png
Source10:	sweethome3d-4.6-script
Source11:	http://sourceforge.net/projects/%{name}/files/TexturesLibraryEditor-source/TexturesLibraryEditor-%{texturesver}-src.zip
Source12:	http://sourceforge.net/projects/%{name}/files/FurnitureLibraryEditor-source/FurnitureLibraryEditor-%{furniturever}-src.zip
Source13:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-textures/Textures-%{textuver}/%{pkgtextu}-Contributions-%{textuver}.zip
Source14:	http://sourceforge.net/projects/%{name}/files/SweetHome3D-textures/Textures-%{textuver}/%{pkgtextu}-eTeksScopia-%{textuver}.zip
Patch0:		sweethome3d-6.1-nomacosx.patch
Patch1:		sweethome3d-6.0-build_xml.patch
Patch2:		sweethome3d-6.1-javadoc.patch
Patch3:		sweethome3d-6.0-disable_checkForUpdates.patch

BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	batik
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix
BuildRequires:	gnu-regexp
BuildRequires:	icedtea-web
BuildRequires:	imagemagick
BuildRequires:	itext-core
BuildRequires:	java-devel >= 1.7.0
BuildRequires:	java-javadoc
BuildRequires:	java3d
BuildRequires:	java3d-javadoc
BuildRequires:	jdepend
BuildRequires:	jdom
BuildRequires:	jiprof
BuildRequires:	junit
BuildRequires:	jpackage-utils
BuildRequires:	sunflow-sweethome3d
BuildRequires:	vecmath
BuildRequires:	xerces-j2
BuildRequires:	xml-commons-apis

Requires:	batik
Requires:	bouncycastle-pkix
Requires:	icedtea-web
Requires:	itext-core
Requires:	java-headless
Requires:	java3d
Requires:	jpackage-utils
Requires:	sunflow-sweethome3d
Requires:	vecmath


%description
Sweet Home 3D is a free interior design application that helps you place your
furniture on a house 2D plan, with a 3D preview.
Available at http://www.sweethome3d.eu/, this program is aimed at people who
want to design their interior quickly, whether they are moving or they just
want to redesign their existing home. Numerous visual guides help you draw the
plan of your home and layout furniture. You may draw the walls of your rooms
upon the image of an existing plan, and then, drag and drop furniture onto the
plan from a catalog organized by categories. Each change in the 2D plan is
simultaneously updated in the 3D view, to show you a realistic rendering of
your layout.

#-----------------------------------------------------------------------------

%package	3dmodels
Summary:	Some extra 3DModels for %{pkgname}
Group:		Graphics/3D
BuildArch:	noarch
Requires:	%{name} >= %{version}-%{release}

%description	3dmodels
Some extra 3DModels for %{pkgname}.

This package contains:
* 3DModels Contributions %{modelver}
* 3DModels KatorLegaz %{modelver}
* 3DModels Scopia %{modelver}
* 3DModels Trees %{modelver}
* 3DModels LucaPresidente %{modelver}
* 3DModels Reallusion-%{modelver}
* 3DModels BlendSwap-CC-BY-%{modelver}
* 3DModels BlendSwap-CC-0-%{modelver}

#-----------------------------------------------------------------------------

%package	textures
Summary:	Some extra Textures for %{pkgname}
Group:		Graphics/3D
BuildArch:	noarch
Requires:	%{name} >= %{version}-%{release}

%description	textures
Some extra Textures for %{pkgname}.

This package contains:
* Textures Contributions %{textuver}
* Textures eTeksScopia %{textuver}

#-----------------------------------------------------------------------------

%package	javadoc
Summary:	Javadoc for %{pkgname}
Group:		Documentation
BuildArch:	noarch

%description	javadoc
Sweet Home 3D - An application for placing your furniture on a house 2D plan,
with a 3D preview

This package contains javadoc for %{pkgname}.

#-----------------------------------------------------------------------------

%prep
%setup -q -n %{pkgname}-%{version}-src
%autopatch -p1

for j in $(find . -name "*.jar"); do
  mv $j $j.no
done

rm -rf lib/windows
rm -rf lib/macosx
rm -rf lib/linux

pushd lib
  ln -sf $(build-classpath batik-all) batik-svgpathparser-1.7.jar
  ln -sf $(build-classpath itext) iText-2.1.7.jar
  ln -sf $(build-classpath java3d/j3dcore) j3dcore.jar
  ln -sf $(build-classpath java3d/j3dutils) j3dutils.jar
  ln -sf $(build-classpath sunflow-0.07.3i) sunflow-0.07.3i.jar
  ln -sf $(build-classpath vecmath) vecmath.jar
# FIXME for package jar that does not exist on Mageia
   mv jmf.jar.no jmf.jar
   mv freehep-vectorgraphics-svg-2.1.1b.jar.no freehep-vectorgraphics-svg-2.1.1b.jar
   mv jeksparser-calculator.jar.no jeksparser-calculator.jar
popd

# Abbot is not building in mga and sweethome3d build without so do add in mageia only if it builds OK
pushd libtest
  ln -sf $(build-classpath gnu-regexp) gnu-regexp-1.1.0.jar
  ln -sf $(build-classpath jdepend) jdepend-2.9.jar
  ln -sf $(build-classpath jdom) jdom-1.0.jar
  ln -sf /usr/share/icedtea-web/netx.jar jnlp.jar
  ln -sf $(build-classpath jiprof/profile) profile.jar
popd

for c in $(find lib -name "*.class"); do
  rm -f $c
done

dos2unix  *.TXT
chmod 644 *.TXT

# for extra 3DModels
mkdir -p 3DModels-Contributions
pushd 3DModels-Contributions
    unzip -q %{SOURCE1}
    mv README.TXT README-3DModels-Contributions.txt
    mv LICENSE.TXT LICENSE-3DModels-Contributions.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-KatorLegaz
pushd 3DModels-KatorLegaz
    unzip -q %{SOURCE2}
    mv README.TXT README-3DModels-KatorLegaz.txt
    mv LICENSE.TXT LICENSE-3DModels-KatorLegaz.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-LucaPresidente
pushd 3DModels-LucaPresidente
    unzip -q %{SOURCE3}
    mv README.TXT README-3DModels-LucaPresidente.txt
    mv LICENSE.TXT LICENSE-3DModels-LucaPresidente.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-Reallusion
pushd 3DModels-Reallusion
    unzip -q %{SOURCE4}
    mv README.TXT README-3DModels-Reallusion.txt
    mv LICENSE.TXT LICENSE-3DModels-Reallusion.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-Scopia
pushd 3DModels-Scopia
    unzip -q %{SOURCE5}
    mv README.TXT README-3DModels-Scopia.txt
    mv LICENSE.TXT LICENSE-3DModels-Scopia.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-Trees
pushd 3DModels-Trees
    unzip -q %{SOURCE6}
    mv README.TXT README-3DModels-Trees.txt
    mv LICENSE.TXT LICENSE-3DModels-Trees.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-BlendSwap-CC-BY
pushd 3DModels-BlendSwap-CC-BY
    unzip -q %{SOURCE7}
    mv README.TXT README-3DModels-BlendSwap-CC-BY.txt
    mv LICENSE.TXT LICENSE-3DModels-BlendSwap-CC-BY.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p 3DModels-BlendSwap-CC-0
pushd 3DModels-BlendSwap-CC-0
    unzip -q %{SOURCE8}
    mv README.TXT README-3DModels-BlendSwap-CC-0.txt
    mv LICENSE.TXT LICENSE-3DModels-BlendSwap-CC-0.txt
    sed -i 's/\r$//' *.txt
popd
# for extra Textures
mkdir -p Textures-Contributions
pushd Textures-Contributions
    unzip -q %{SOURCE13}
    mv README.TXT README-Textures-Contributions.txt
    mv LICENSE.TXT LICENSE-Textures-Contributions.txt
    sed -i 's/\r$//' *.txt
popd
mkdir -p Textures-eTeksScopia
pushd Textures-eTeksScopia
    unzip -q %{SOURCE14}
    mv README.TXT README-Textures-eTeksScopia.txt
    mv LICENSE.TXT LICENSE-Textures-eTeksScopia.txt
    sed -i 's/\r$//' *.txt
popd

%build
%ant application furniture textures help javadoc

%install
# .jar-repertory
mkdir -p %{buildroot}%{_javadir}/%{name}
install -pm 644 build/SweetHome3D.jar \
  %{buildroot}%{_javadir}/%{name}/%{pkgname}-%{version}.jar

(
  cd %{buildroot}%{_javadir}/%{name}
  for jar in *-%{version}*; do
    ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`
  done
)

for i in Furniture Textures Help; do
    install -pm 644 build/$i.jar %{buildroot}%{_javadir}/%{name}
done

rm -rf lib/iText-2.1.7.jar
rm -rf lib/j3dcore.jar
rm -rf lib/j3dutils.jar
rm -rf lib/sunflow-0.07.3i.jar
rm -rf lib/vecmath.jar
rm -rf lib/Loader3DS1_2u.jar

# FIXME for package jar that does not exist on Mageia
install -pm 644 lib/jmf.jar %{buildroot}%{_javadir}/%{name}
install -pm 644 lib/freehep-vectorgraphics-svg-2.1.1b.jar %{buildroot}%{_javadir}/%{name}
install -pm 644 lib/jeksparser-calculator.jar %{buildroot}%{_javadir}/%{name}
# FIXME for display the sweethome3d splash screen
install -pm 644 libtest/jnlp.jar.no %{buildroot}%{_javadir}/%{name}/jnlp.jar

# 3Dmodels-repertory
mkdir -p %{buildroot}%{_datadir}/%{name}/%{pkgmod}
for i in Contributions KatorLegaz LucaPresidente Reallusion Scopia Trees BlendSwap-CC-BY BlendSwap-CC-0; do
    install -m 644 3DModels-$i/*.sh3f %{buildroot}%{_datadir}/%{name}/%{pkgmod}
done

# Textures-repertory
mkdir -p %{buildroot}%{_datadir}/%{name}/%{pkgtextu}
for i in Contributions eTeksScopia; do
    install -m 644 Textures-$i/*.sh3t %{buildroot}%{_datadir}/%{name}/%{pkgtextu}
done

# javadoc-repertory
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}

# binary-repertory
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE10} %{buildroot}%{_bindir}/%{name}

# icons-repertory
mkdir -p %{buildroot}%{_datadir}/pixmaps %{buildroot}%{_iconsdir} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/
cp -pr %{SOURCE9} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png
cp -pr %{SOURCE9} %{buildroot}%{_datadir}/pixmaps/%{name}.png
cp -pr deploy/%{pkgname}*.jpg %{buildroot}%{_iconsdir}
cp -pr deploy/%{pkgname}*.gif %{buildroot}%{_iconsdir}

for png in 64x64 32x32 22x22 16x16; do
  mkdir -p %{buildroot}%{_iconsdir}/hicolor/${png}/apps/
  convert -geometry $png %{SOURCE9} %{buildroot}%{_iconsdir}/hicolor/${png}/apps/%{name}.png
done

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=Sweet Home 3D
Name[fr]=Sweet Home 3D
Name[pt]=Sweet Home 3D
Name[ru]=Милый дом 3D
GenericName=Sweet Home 3D
GenericName[fr]=Sweet Home 3D
GenericName[ru]=Проектирование домашнего интерьера в 3D
Comment=Design Application
Comment[fr]=Application de conception d'intérieur en 3D
Comment[pt]=Aplicativo de design de interiores
Comment[ru]=Программа проектирования домашнего интерьера в 3D
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
StartupWMClass=com-eteks-sweethome3d-SweetHome3D
Categories=Application;Graphics;2DGraphics;3DGraphics;
MimeType=application/vnd.sh3d;
EOF

desktop-file-install --mode=0644 --dir=%{buildroot}%{_datadir}/applications %{name}.desktop

# mime-entry for sh3d files
mkdir -p %{buildroot}%{_datadir}/mime/packages
cat > %{buildroot}%{_datadir}/mime/packages/%{name}.xml <<EOF
<?xml version="1.0"?>
<mime-info xmlns='http://www.freedesktop.org/standards/shared-mime-info'>
        <mime-type type="application/vnd.sh3d">
                <comment>SweetHome3D Project</comment>
                <glob pattern="*.sh3d"/>
        </mime-type>
</mime-info>
EOF

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING* LICENSE.TXT README.TXT
%{_bindir}/%{name}
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/Furniture.jar
%{_javadir}/%{name}/Help.jar
%{_javadir}/%{name}/%{pkgname}-%{version}.jar
%{_javadir}/%{name}/%{pkgname}.jar
%{_javadir}/%{name}/Textures.jar
# FIXME for package jar that does not exist on Mageia
%{_javadir}/%{name}/jmf.jar
%{_javadir}/%{name}/freehep-vectorgraphics-svg-2.1.1b.jar
%{_javadir}/%{name}/jeksparser-calculator.jar
# FIXME for display the sweethome3d splash screen
%{_javadir}/%{name}/jnlp.jar
#
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/*.jpg
%{_iconsdir}/*.gif
%{_iconsdir}/hicolor/*x*/apps/%{name}.png

%files 3dmodels
%doc 3DModels-Contributions/*.txt 3DModels-KatorLegaz/*.txt 3DModels-Scopia/*.txt 3DModels-Trees/*.txt 3DModels-LucaPresidente/*.txt 3DModels-Reallusion/*.txt 3DModels-BlendSwap-CC-BY/*.txt 3DModels-BlendSwap-CC-0/*.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{pkgmod}
%{_datadir}/%{name}/%{pkgmod}/*.sh3f

%files textures
%doc Textures-Contributions/*.txt Textures-eTeksScopia/*.txt
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{pkgtextu}
%{_datadir}/%{name}/%{pkgtextu}/*.sh3t

%files javadoc
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*


%changelog
* Fri Jan 25 2019 daviddavid <daviddavid> 6.1-1.mga7
+ Revision: 1360616
- new version: 6.1 (mga#24232)
- rename and rediff P0 and P2 to adapt 6.1 version

* Thu Jan 03 2019 daviddavid <daviddavid> 6.0-1.mga7
+ Revision: 1348839
- new version: 6.0
- new version of extra 3DModels: 1.6.4
- rename and rediff all patches to adapt 6.0 version
- switch again to system SunFlow (sunflow-sweethome3d)

* Sun Sep 23 2018 daviddavid <daviddavid> 5.7-2.mga7
+ Revision: 1297215
- use embedded forked SunFlow:
  * Sweet Home 3D is built with a version forked from SunFlow 0.07.3
  * https://sourceforge.net/p/sweethome3d/bugs/851/
+ umeabot <umeabot>
- Mageia 7 Mass Rebuild

* Mon Mar 26 2018 daviddavid <daviddavid> 5.7-1.mga7
+ Revision: 1212523
- new version: 5.7
- rename and rediff all patches to adapt 5.7 version

* Sat Jan 13 2018 daviddavid <daviddavid> 5.6-1.mga7
+ Revision: 1192476
- new version: 5.6
- new version of extra 3DModels: 1.6.3
- rename and rediff P0 and P3 to adapt 5.6 version

* Fri Feb 17 2017 daviddavid <daviddavid> 5.4-1.mga6
+ Revision: 1086617
- new version: 5.4
- new version of extra Textures: 1.2
- rename and rediff all patches to adapt 5.4 version

* Wed Nov 30 2016 daviddavid <daviddavid> 5.3-2.mga6
+ Revision: 1071246
- fix missing bcpkix classpath entry

* Tue Nov 29 2016 daviddavid <daviddavid> 5.3-1.mga6
+ Revision: 1070935
- new version: 5.3
- new version of extra 3DModels: 1.6.2
- rename and rediff all patches to adapt 5.3 version

* Tue Mar 15 2016 daviddavid <daviddavid> 5.2-2.mga6
+ Revision: 990909
- rediff javadoc patch (since fixed autopatch)

* Sun Feb 21 2016 daviddavid <daviddavid> 5.2-1.mga6
+ Revision: 975088
- new version: 5.2
- new version of extra 3DModels: 1.6.1

* Mon Feb 15 2016 daviddavid <daviddavid> 5.1-3.mga6
+ Revision: 960767
- new version of extra 3DModels: 1.6

* Mon Dec 21 2015 zezinho <zezinho> 5.1-2.mga6
+ Revision: 912808
- add sh3d mime type to allow opening files directly from file browsers
- add portuguese translation to the desktop file

* Tue Oct 06 2015 daviddavid <daviddavid> 5.1-1.mga6
+ Revision: 886531
- new version: 5.1
- rename and rediff all patches to adapt 5.1 version

* Fri Jul 31 2015 daviddavid <daviddavid> 5.0-1.mga6
+ Revision: 859992
- new version: 5.0
- rename and rediff all patches to adapt 5.0 version
- add Patch3 to disable checkForUpdates option
- fix ant build without AppleJavaExtensions.jar (improved of nomacosx.patch)

* Tue Feb 10 2015 daviddavid <daviddavid> 4.6-1.mga5
+ Revision: 814603
- new version: 4.6
- new version of extra 3DModels: 1.5.1
- rename and rediff all patches to adapt 4.6 version
- rename script for 4.6 version
- remove no more needed build-classpath on java3ds-fileloader

* Tue Jan 13 2015 daviddavid <daviddavid> 4.5-4.mga5
+ Revision: 810460
- new version of extra 3DModels: 1.5
- update requirements

* Fri Dec 26 2014 daviddavid <daviddavid> 4.5-3.mga5
+ Revision: 806148
- attribute the sweethome3d-javadoc package to Documentation group

* Fri Nov 21 2014 alexl <alexl> 4.5-2.mga5
+ Revision: 798188
- translated GenericName[ru]

* Sun Oct 26 2014 daviddavid <daviddavid> 4.5-1.mga5
+ Revision: 793502
- new version: 4.5
- new version of extra 3DModels: 1.4.2
- new version of extra Textures: 1.1
- rename and rediff patches to adapt 4.5 version
- remove java3ds-fileloader from script, build and runtime deps
  * 4.5 replaces Loader3DS with a library inspired from lib3ds

* Wed Oct 15 2014 umeabot <umeabot> 4.4-4.mga5
+ Revision: 742106
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 4.4-3.mga5
+ Revision: 689637
- Mageia 5 Mass Rebuild

* Sat Jul 12 2014 daviddavid <daviddavid> 4.4-2.mga5
+ Revision: 651436
- new version of extra 3DModels: 1.4.1
- new version of extra Textures: 1.0.1

* Tue Jun 17 2014 daviddavid <daviddavid> 4.4-1.mga5
+ Revision: 637851
- create new pathes for 4.4 version
- use apply_patches macro
- change the upstream sunflow version for classpath
- new version: 4.4

* Sun May 18 2014 daviddavid <daviddavid> 4.3-5.mga5
+ Revision: 623596
- remove obsolete suggests pkg on libcg0
- new version of extra 3DModels: 1.4

* Tue Mar 04 2014 david-david <david-david> 4.3-4.mga5
+ Revision: 599535
- remove janino package as Required (bug mga#12541)
- remove janino package on start script too (line 6)
- fix display for sweethome3d splash screen
- add some extra Textures version 1.0 for sweethome3d (NEW)
- add some extra textures on start script too (NEW) (line 29 to 41)
+ pterjan <pterjan>
- Fix itext dependency

* Sun Feb 09 2014 joequant <joequant> 4.3-3.mga5
+ Revision: 587181
- add java-devel to requires

* Sun Feb 09 2014 joequant <joequant> 4.3-2.mga5
+ Revision: 587090
- add version for java-devel

* Sun Jan 19 2014 joequant <joequant> 4.3-1.mga4
+ Revision: 566896
- fix revision number
- upgrade to 4.3

* Sun Jan 05 2014 dmorgan <dmorgan> 4.2-3.mga4
+ Revision: 564799
- Rebuild to please autobuild

* Sun Jan 05 2014 dmorgan <dmorgan> 4.2-2.mga4
+ Revision: 564676
- Remove abbot support

* Sat Dec 07 2013 joequant <joequant> 4.2-1.mga4
+ Revision: 555764
- update patches
- upgrade to version 4.2
+ umeabot <umeabot>
- Mageia 4 Mass Rebuild

* Mon Oct 07 2013 joequant <joequant> 4.1-1.mga4
+ Revision: 492411
- imported package sweethome3d


* Thu Jun 09 2011 gil <gil> 3.2-2.%%mkrel
- add abbot support
- add javadoc sub package

* Wed Jun 08 2011 gil <gil> 3.2-1.%%mkrel
- add freehep-{util,io,xml} java3ds-fileloader vectorgraphics support

* Wed Jun 01 2011 gil <gil> 3.2-0.%%mkrel
- initial rpm