#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jatl
Version  : 0.2.2
Release  : 1
URL      : https://github.com/agentgt/jatl/archive/jatl-0.2.2.tar.gz
Source0  : https://github.com/agentgt/jatl/archive/jatl-0.2.2.tar.gz
Source1  : https://repo.gradle.org/gradle/libs-releases/com/googlecode/jatl/jatl/0.2.2/jatl-0.2.2.jar
Source2  : https://repo.gradle.org/gradle/libs-releases/com/googlecode/jatl/jatl/0.2.2/jatl-0.2.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-jatl-data = %{version}-%{release}
Requires: mvn-jatl-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jatl package.
Group: Data

%description data
data components for the mvn-jatl package.


%package license
Summary: license components for the mvn-jatl package.
Group: Default

%description license
license components for the mvn-jatl package.


%prep
%setup -q -n jatl-jatl-0.2.2

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jatl
cp COPYING %{buildroot}/usr/share/package-licenses/mvn-jatl/COPYING
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/jatl/jatl/0.2.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/jatl/jatl/0.2.2/jatl-0.2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/jatl/jatl/0.2.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/jatl/jatl/0.2.2/jatl-0.2.2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/googlecode/jatl/jatl/0.2.2/jatl-0.2.2.jar
/usr/share/java/.m2/repository/com/googlecode/jatl/jatl/0.2.2/jatl-0.2.2.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jatl/COPYING
