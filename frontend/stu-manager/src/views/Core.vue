<template> 
  <div id="core-box">
    <el-table
      :data.sync="tableData"
      style="width: 800px">
      <el-table-column
        v-for="item in tableMeta"
        :label="item.label"
        :prop="item.prop"
        :key="item.sno"
        :width="item.width"
        align="center"
      ></el-table-column>
      <el-table-column
        align="right"
        width="180px">
        <template slot="header" slot-scope="scope">
          <el-input
            v-model="search"
            size="mini"
            @keyup.enter.native="searchStu()"
            placeholder="输入用户名或学号搜索"/>
        </template>
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="editInfo(scope.$index, scope.row)">Edit</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="delInfo(scope.$index, scope.row)">Delete</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-button class="new" @click="newInfo" size="small ">新增</el-button>

    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page.sync="pagination.currentPage"
      :page-sizes="[8]"
      :page-size="100"
      layout="total, sizes, prev, pager, next, jumper"
      :total="pagination.total">
    </el-pagination>

  </div>
</template>

<script>
// 创建时间: 2020/11/27

export default {
  name: "Core",
  
  data() {
    let mockTableDataItem = {
      sno: 1801130161,
      sname: 'juln',
      sex: 'male',
      age: 20,
      pro: '软件工程',
      address: '上海市普陀区金沙江路 1518 弄'
    }
    return {
      tableMeta: [
        {label:'学号',prop:'sno',width:'100px'},
        {label:'姓名',prop:'sname',width:'100px'},
        {label:'性别',prop:'sex',width:'60px'},
        {label:'年龄',prop:'age',width:'50px'},
        {label:'专业',prop:'pro',width:'100px'},
        {label:'地址',prop:'address',width:'210px'},
      ],
      tableData: [
        mockTableDataItem,mockTableDataItem,
        mockTableDataItem,mockTableDataItem,
        mockTableDataItem,mockTableDataItem,
        ,mockTableDataItem,,mockTableDataItem
      ],
      search: '',
      pagination: {
        currentPage: 1,
        total: 400,
      }
    }
  },

  created() {
    this.$http.get('/manager/getTotalNo').then(result => {
      this.pagination.total = result.data.data.number * 1
    })
    this.$http.get('manager/find',{
      startIndex: 0,
      size: 8
    }).then(result => {
      this.tableData = result.data.data
    })
  },

  methods: {
    searchStu() {
      this.$http.get(`/manager/findStuBySnoOrSname?keyword=${this.search}`)
      .then(res => {
        console.log(res)
        this.tableData = [res.data.data]
      })
    },
    popTable(data={},confirmFun,cancelFun) {
      this.$alert(`
          <table class='new-table'>
            <tr>
              <td><span>学号:</span></td>
              <td><input type='text' value='${data.sno||''}' placeholder='请输入学号' name="sno" /></td>
            </tr>
            <tr>
              <td><span>姓名:</span></td>
              <td><input type='text' value='${data.sname||''}' placeholder='请输入姓名' name="sname" /></td>
            </tr>
            <tr>
              <td><span>性别:</span></td>
              <td><input type='radio' ${data.sex===undefined?'checked':(data.sex==='male'?'checked':'')} value="male" name="sex" /> 男 &nbsp; <input type='radio' ${data.sex===undefined?'':(data.sex==='female'?'checked':'')} value="female" name="sex" /> 女</td>
            </tr>
            <tr>
              <td><span>年龄:</span></td>
              <td><input type='text' value='${data.age||''}' placeholder='请输入年龄' name="age" /></td>
            </tr>
            <tr>
              <td><span>专业:</span></td>
              <td><input type='text' value='${data.pro||''}' placeholder='请输入专业' name="pro" /></td>
            </tr>
            <tr>
              <td><span>地址:</span></td>
              <td><input type='text' value='${data.address||''}' placeholder='请输入地址' name="address" /></td>
            </tr>
          </table>
        `, 
        '新增学生信息', {
        dangerouslyUseHTMLString: true,
        callback: action => {
          const $ = str=>document.querySelector(str)
          let data = {
            sno: $('.new-table input[name=sno]').value,
            sname: $('.new-table input[name=sname]').value,
            sex: $('.new-table input[name=sex]').value,
            age: $('.new-table input[name=age]').value,
            pro: $('.new-table input[name=pro]').value,
            address: $('.new-table input[name=address]').value,
          }
          if(action === 'confirm') {
            // 上传数据, 新增学生信息
            confirmFun(data)
          }
          else{
            cancelFun(data)
          }
        }
      })
    },
    editInfo(index, row) {
      let beforeSno = row.sno
      this.popTable(row, (data) => {
        data.beforeSno = beforeSno
        // 网络请求修改
        this.$http.post('/manager/update',data).then(result => {
          if(result.data.data.msg === 'success') {
            this.$message({
              message: '添加成功',
              showClose: true,
              type: 'success'
            })
            // 本页面的缓存数据删除
            let newTableData = []
            Object.assign(newTableData,this.tableData)
            newTableData[index] = data
            this.tableData = newTableData
          }
          else{
            this.$message({
              message: '添加失败',
              showClose: true,
              type: 'error'
            })
          }
        })
      },
      () => {

      })
    },
    delInfo(index, row) {
      // 网络请求删除
      this.$http.get('/manager/delete?sno='+row.sno).then(result => {
        if(result.data.data.msg === 'success') {
          this.$message({
            message: '删除成功',
            type: 'success'
          })
          // 本页面的缓存数据删除
          for(let i = 0; i < this.tableData.length; i++) {
            if(this.tableData[i] == row) {
              this.tableData.splice(index,1)
              break
            }
          }
        }
        else{
          this.$message({
            message: '删除失败',
            showClose: true,
            type: 'error'
          })
        }
      })
    },
    newInfo() {
      this.popTable(undefined, (data) => {
        this.$http.post('/manager/new',data).then(result => {
          if(result.data.data.msg === 'success') {
            this.$message({
              message: '添加成功',
              showClose: true,
              type: 'success'
            })
            // 本页面的缓存数据添加
            this.tableData.push(data)
          }
          else{
            this.$message({
              message: '添加失败',
              showClose: true,
              type: 'error'
            })
          }
        })
      },
      () => {
        
      })
    },
    handleSizeChange() {

    },
    handleCurrentChange() {
      let currentPage = this.pagination.currentPage
      let size = 8
      let startIndex = (currentPage-1) * size
      console.log({startIndex,size})
      this.$http.get(`/manager/find?startIndex=${startIndex}&size=${size}`).then(result => {
        this.tableData = result.data.data
      })
    }
  },
  
  components: {
      
  },
}
</script>

<style scoped lang="less">
[v-cloak] {
  display: none;
}
.el-table{
  @theadBg: rgba(0,0,0,.05);
  @tbodyBg: rgba(255,255,255,.1);
  @selectBg: rgba(255,255,255,.2);
  margin: 20px auto;
  border-radius: 5px;
  box-shadow: 1px 1px 15px black;
  overflow: hidden;
  background-color: initial !important;
  *{
    background-color: initial !important;
  }
  /deep/ *{
    background-color: initial !important;
  }
  // 
  /deep/ thead{
    tr{
      background-color: @theadBg !important;
      th{
        background-color: @theadBg !important;
      }
    }
  }
  /deep/ tbody{
    font-size: 13px;
    .el-table__row{
      background-color: @tbodyBg !important;
    }
    // .el-table__row--striped{
    //   background-color: @tbodyBg !important;
    //   td{
    //     background-color: @tbodyBg !important;
    //   }
    // }
    .current-row{
      td{
        background-color: @tbodyBg !important;
      }
    }
  }
}

.el-button.new{
  margin: auto;
  display: block;
  background-color: rgba(255,255,255,.1);
}

.el-pagination{
  margin: 20px auto;
  width: 550px;
  /deep/ *{
    color: white;
  }
  /deep/ .btn-prev,
  /deep/ .btn-next,
  /deep/ .el-pager li,
  /deep/ .el-input__inner{
    background-color: rgba(255,255,255,.1) !important;
  }
  /deep/ .el-icon-more{
    color: white;
  }
}

</style>