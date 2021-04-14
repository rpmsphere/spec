Name:           bluej-extensions
Summary:        Various extensions for bluej
Version:        20110529
Release:        7.1
License:        Freely available to anyone as is for use and non-commercial distribution
URL:            http://www.bluej.org/extensions/extensions.html
Group:          Development/Tools/IDE
BuildArch:      noarch
BuildRequires:  unzip
BuildRequires:  tar
Requires:       bluej
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define         extension_dir %{_datadir}/bluej/extensions/
Source0:        bluej-extensions-20110529.tar.bz2
Source1:        extension_list.txt
Source2:        update_extensions.sh

%description
BlueJ offers an extension API that allows third parties to develop extensions
to the environment. Extensions offer additional functionality not included in
the core system.

#----------------------------------------------------------------------

%package class_card
Summary:        Class Card - A Better UML Extension 
Group:          Development/Tools/IDE
Requires:       bluej
URL:            http://klassenkarte.steinhuber.de/files/Klassenkarte.jar

%description class_card
An improvement over the original UML Extension, this one allows you to show
more than one class display, and to move class displays around the screen.
Available in English and German.

Author:
-------
    Michael Steinhuber


%files class_card
%defattr(-,root,root)
%{extension_dir}/Klassenkarte.jar

#----------------------------------------------------------------------

%package multiproject
Summary:        A Multi-Project Workspace Handler  
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://multiproject.sourceforge.net/

%description multiproject
This BlueJ extension allows you to easily manage (i.e. create, import/export
and switch between) multiple BlueJ projects. Some neat features help you to
auto-position package windows or to handle bunches of jar files economically
(e.g. when correcting students' exercises).


%files multiproject
%defattr(0644,root,root,0755)
%doc multiproject.pdf
%defattr(-,root,root)
%{extension_dir}/multiproject.jar

#----------------------------------------------------------------------

%package rolesOfVariables
Summary:        Identifying the roles of variables 
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://www.bluej.org/extensions/files/rolesOfVariables.zip

%description rolesOfVariables
The Roles of Variables BlueJ extension is based on Sajaniemi's Roles of
Variables theory, which describes the common ways in which variables are used
in programming. The extension allows users to annotate their programs with
labels based on these roles, and uses an automated system to check whether the
actual use of the variable is consistent with that role assignment.


%files rolesOfVariables
%defattr(0644,root,root,0755)
%doc RoV_training_files.zip rolesOfVariables-README.txt BishopDissertation.pdf koliPaper.pdf
%defattr(-,root,root)
%{extension_dir}/roles_of_variables.jar
%dir %{extension_dir}/RoVs
%dir %{extension_dir}/RoVs_Javadocs
%{extension_dir}/RoVs/*
%{extension_dir}/RoVs_Javadocs/*

#----------------------------------------------------------------------

%package CNUBlueJFormatterInstaller25x
Summary:        CNU BlueJ Code Formatter
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://cnubluej.pcs.cnu.edu/CNUBlueJFormatterInstaller25x.jar

%description CNUBlueJFormatterInstaller25x
CNU BlueJ formatter is a BlueJ extension that integrates Eclipse's code style
formatting capabilities into BlueJ's editor. The formatter adds a "Format"
button to the editor, and formats compiled source code according to a set of
style properties specified in a properties file. These properties can be
customized using a simple dialog interface accessible from BlueJ's Preferences
option. For convenience, the formatter comes with an installation executable
JAR file.


%files CNUBlueJFormatterInstaller25x
%defattr(-,root,root)
%{extension_dir}/CNUBlueJFormatterInstaller25x.jar

#----------------------------------------------------------------------

%package objectdrawinvoker
Summary:        Objectdrawinvoker
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://www.bluej.org/extensions/files/objectdrawinvoker.jar

%description objectdrawinvoker
An extension to make it easier to work with the objectdraw library. If any
class in a BlueJ class diagram extends the objectdraw Controller class, this
extension adds a menu item to the class which will create an object, place it
on the BlueJ object bench and invoke its startController() method. I.e. "run"
it inside BlueJ rather than as an external Applet.


%files objectdrawinvoker
%defattr(-,root,root)
%{extension_dir}/objectdrawinvoker.jar

#----------------------------------------------------------------------

%package  	MainRunner
Summary:        Main Program Runner 
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://www.bluej.org/extensions/files/MainRunner.jar

%description 	MainRunner
An extension to allow direct invocation of a main method. If a class contains a
properly declared main method, this extensions adds a menu item "Run Main
Method" which directly invokes it. This makes the main method much more
obvious, if that suits your style, and also helps you get the declaration
right; if it's not public static void main(String [] args) you won't see the
menu item. 


%files 	MainRunner
%defattr(-,root,root)
%{extension_dir}/MainRunner.jar

#----------------------------------------------------------------------

%package SyntaxSourcePrinter
Summary:        Syntax Source Printer
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://www.bluej.org/extensions/files/SyntaxSourcePrinter.jar

%description SyntaxSourcePrinter
Supports colour printing of source code from within BlueJ using the syntax
colouring used in BlueJ's editor. This new version not only sends source code
to printers, but also saves HTML or RTF to files, for inclusion in course notes
or slides.

The extension adds a new "Print" menu item to the context menu of classes in
the BlueJ Class Diagram. It obeys the colour settings in the file moe.defs. 


%files SyntaxSourcePrinter
%defattr(-,root,root)
%{extension_dir}/SyntaxSourcePrinter.jar

#----------------------------------------------------------------------

%package ACMInvoker
Summary:        ACM Invoker 
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://www.bluej.org/extensions/ACMInvoker/ACMInvoker.jar

%description ACMInvoker
An extension to make it easier to work with the ACM Java Task Force library. 

If any class in a BlueJ class diagram implements the acm.program.Program class,
this extension adds a menu item to the class which will create an object, place
it on the BlueJ object bench and invoke its start() method. I.e. "run" it
inside BlueJ rather than as an external Applet.


%files ACMInvoker
%defattr(-,root,root)
%{extension_dir}/ACMInvoker.jar

#----------------------------------------------------------------------

%package Checkstyle
Summary:        Checking of coding styles
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://bluejcheckstyle.sourceforge.net/

%description Checkstyle
Allows automated checking of coding styles. Coding styles can be specified
flexibly in an external file. This is a major update to this extension,
including:

 * Now uses the latest Checkstyle release, v4.3
 * Simpler one-jar installation
 * Allows configuration files to be read from URLs in addition to local files
 * The documentation has additional tips useful for lab-based or cloned setup


%files Checkstyle
%defattr(-,root,root)
%{extension_dir}/checkstyle-extension-4.3-0.jar

#----------------------------------------------------------------------

%package patterncoder
Summary:        A Design Patterns Extension 
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://www.patterncoder.org/

%description patterncoder
Provides a wizard which guides the user through the process of adding a Design
Pattern or binary class relationship to a BlueJ project. The user can select a
pattern or relationship and choose specific names for the component classes. A
set of basic classes are then generated. The classes have sufficient code
out-of-the-box to allow exploration of the behaviour with no additional coding.

They can then be edited to meet the requirements of specific problems. A
selection of patterns and relationships is provided, and other patterns can be
defined using XML files and added into the extension.


%files patterncoder
%defattr(0644,root,root,0755)
%doc guide.pdf
%defattr(-,root,root)
%{extension_dir}/PatternCoder.jar
%{extension_dir}/PatternFiles
%{extension_dir}/javadoc
%{extension_dir}/src

#----------------------------------------------------------------------

%package ClassWizard
Summary:        A Class Wizard
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
Requires:       java >= 1.5.0
URL:            http://www.bluej.or.kr/

%description ClassWizard
The "Class Wizard" enables BlueJ users to quickly and easily create or edit
classes and class' components (attributes, methods, constructors, and so on)
using the syntax of UML. The Wizard can be used before or after creating
classes and editing their source code in the BlueJ text editor.


%files ClassWizard
%defattr(-,root,root)
%{extension_dir}/ClassWizard.jar

#----------------------------------------------------------------------

%package UMLextension
Summary:     UML Extension 
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       bluej
URL:            http://www.bluej.org/extensions/UMLextension/index.html

%description UMLextension
Displays a simple popup for a BlueJ class in the form of a UML Class icon.
Details of what will be displayed, and the precise syntax used can be
configured via the preferences panel, or the BlueJ properties files. 


%files UMLextension
%defattr(-,root,root)
%{extension_dir}/UMLextension.jar

#----------------------------------------------------------------------

%prep
%setup -q 
for file in *.zip ; do
	unzip $file
	rm $file
done
for file in *.tar.gz ; do
	tar -xf $file
	rm $file
done
#
mv patterncoder_0.5.3/* .
rmdir patterncoder_0.5.3
#
mv rolesOfVariables/* .
find . -name .DS_Store -delete
find . -name *~ -delete
find . -name .project -delete
find . -name .classpath -delete
rmdir rolesOfVariables
mv README.txt rolesOfVariables-README.txt

%build

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p $RPM_BUILD_ROOT/%{extension_dir}
cp -r * $RPM_BUILD_ROOT/%{extension_dir}/
# cleanup the mess
rm -rf $RPM_BUILD_ROOT/%{extension_dir}/__MACOSX*
# documentation
install -m644 %{SOURCE1} .
install -m644 %{SOURCE2} .
for file in  RoV_training_files.zip rolesOfVariables-README.txt *.pdf ; do
	find $RPM_BUILD_ROOT/%{extension_dir}/ -name "$file" -exec mv -v {} . \;
done
mv $RPM_BUILD_ROOT/%{extension_dir}/papers/*.pdf .
rmdir $RPM_BUILD_ROOT/%{extension_dir}/papers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %{_datadir}/bluej
%doc extension_list.txt update_extensions.sh
%dir %{extension_dir}

%changelog
* Tue Jul 24 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20110529
- Rebuilt for Fedora

* Thu Jul 30 2009 lars@linux-schulserver.de
- initial package
